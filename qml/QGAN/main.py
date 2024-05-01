import pennylane as qml
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt


seed = 1234
np.random.seed(seed)
torch.manual_seed(seed)


class QGAN_PENNYLANE:
    """
    Overview and steps for QGAN:

    1. Prepare |psi_1> on q0, which is the input to QGAN. the preparation is a black box, and we want to guess the state using the GAN.
        - We can obtain any number of |psi_1>s from the black box.
    2. A Quantum Generator will run on q0, preparing a state |psi_g> close to |psi_1>.
        - This will be implemented using a variational form dependent on some trainable parameters.
    3. A Quantum Discriminator will run on q0 and q1.
        - May take |psi_1> or generated-state as input.

    Since both modules (generator and discriminator) work with quantum data, we don't need feature maps.
    They only need to consist of variational forms, and measurements if necessary.
    """

    def __init__(self):
        state_0 = [[1], [0]]
        self.M = state_0 * np.conj(state_0).T

    def prepare_true_state(self):
        """
        using the universal one qubit gate: $U_3(\phi, \theta, \delta)$
        """
        phi = np.pi / 3
        theta = np.pi / 4
        delta = np.pi / 5
        qml.U3(theta, phi, delta, wires=0)

    def generator(self, weights):
        """
        using the parameterized universal one qubit gate
        """
        qml.U3(weights[0], weights[1], weights[2], wires=0)

    def discriminator(self, nqubits, weights, reps=1):
        """
        Variation of the two-local variation form
        """
        param_index = 0  # index for parameters

        # Initial Rotations
        for r in range(reps):
            for q in range(nqubits):
                qml.RX(weights[param_index], wires=q)
                param_index += 1
                qml.RY(weights[param_index], wires=q)
                param_index += 1
                qml.RZ(weights[param_index], wires=q)
                param_index += 1

        # Entanglements
        for q in range(nqubits - 1):
            qml.CNOT(wires=[q, q + 1])

        # Final Rotations
        for r in range(reps):
            for q in range(nqubits):
                qml.RX(weights[param_index], wires=q)
                param_index += 1
                qml.RY(weights[param_index], wires=q)
                param_index += 1
                qml.RZ(weights[param_index], wires=q)
                param_index += 1


if __name__ == "__main__":
    wires = 2

    qgan = QGAN_PENNYLANE()

    dev = qml.device("default.qubit", wires=wires)

    @qml.qnode(dev, intergace="torch", diff_method="backprop")
    def true_discriminator(weights_dis):
        qgan.prepare_true_state()
        qgan.discriminator(nqubits=wires, weights=weights_dis)
        return qml.expval(qml.Hermitian(qgan.M, wires=[0]))

    @qml.qnode(dev, intergace="torch", diff_method="backprop")
    def generator_discriminator(weights_gen, weights_dis):
        qgan.generator(weights=weights_gen)
        qgan.discriminator(nqubits=wires, weights=weights_dis)
        return qml.expval(qml.Hermitian(qgan.M, wires=[0]))

    def discriminator_loss(weights_gen, weights_dis):
        out_gen = generator_discriminator(weights_gen, weights_dis)
        out_true = true_discriminator(weights_dis)
        return -(torch.log(1 - out_gen) + torch.log(out_true)) / 2

    def generator_loss(weights_gen, weights_dis):
        out_gen = generator_discriminator(weights_gen, weights_dis)
        return -torch.log(out_gen)

    # weights of the model
    weights_gen = torch.rand(3, requires_grad=True)
    weights_dis = torch.rand((3 + 1) * 2 * 3, requires_grad=True)

    # optimizers
    optg = torch.optim.SGD([weights_gen], lr=0.5)
    optd = torch.optim.SGD([weights_dis], lr=0.5)

    # training
    dis_losses = []  # Discriminator losses.
    gen_losses = []  # Generator losses.
    log_weights = []  # Generator weights.
    ncycles = 150  # Number of training cycles.

    for i in range(ncycles):
        # Train the discriminator.
        optd.zero_grad()
        lossd = discriminator_loss(weights_gen.detach(), weights_dis)
        lossd.backward()
        optd.step()
        # Train the generator.
        optg.zero_grad()
        lossg = generator_loss(weights_gen, weights_dis.detach())
        lossg.backward()
        optg.step()
        # Log losses and weights.
        lossd = float(lossd)
        lossg = float(lossg)
        dis_losses.append(lossd)
        gen_losses.append(lossg)
        log_weights.append(weights_gen.detach().clone().numpy())
        # Print the losses every fifteen cycles.
        if np.mod((i + 1), 15) == 0:
            print("Epoch", i + 1, end=" ")
            print("| Discriminator loss:", round(lossd, 4), end=" ")
            print("| Generator loss:", round(lossg, 4))

    epochs = np.array(range(len(gen_losses))) + 1
    plt.plot(epochs, gen_losses, label="Generator loss")
    plt.plot(epochs, dis_losses, label="Discriminator loss")
    plt.xlabel("Epoch")
    plt.legend()
    plt.show()