import pennylane as qml
from pennylane import qaoa
from pennylane import numpy as np

H0 = qml.PauliX(0) + qml.PauliX(1)
H1 = 1.0 * qml.PauliZ(0) @ qml.PauliZ(1)
wires = range(2)
dev = qml.device("lightning.qubit", wires=wires)
p = 2


@qml.qnode(dev)
def energy(angles):
    for w in wires:
        qml.Hadamard(wires=w)
    for i in range(p):
        qaoa.cost_layer(angles[2 * i + 1], H1)
        qaoa.mixer_layer(angles[2 * i], H0)
    return qml.expval(H1)


optimizer = qml.GradientDescentOptimizer()
steps = 20
angles = np.array([1.0, 1.0, 1.0, 1.0], requires_grad=True)
for i in range(steps):
    angles = optimizer.step(energy, angles)
print("Optimal angles", angles)


@qml.qnode(dev)
def sample_solutions(angles):
    for w in wires:
        qml.Hadamard(wires=w)
    for i in range(p):
        qaoa.cost_layer(angles[2 * i + 1], H1)
        qaoa.mixer_layer(angles[2 * i], H0)
    return qml.sample()


print(sample_solutions(angles, shots=5))
