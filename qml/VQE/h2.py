from jax import numpy as np
import jax
import pennylane as qml

jax.config.update("jax_platform_name", "cpu")
jax.config.update("jax_enable_x64", True)

# Building the electronic Hamiltonian
symbols = ["H", "H"]
coordinates = np.array([0.0, 0.0, -0.6614, 0.0, 0.0, 0.6614])

H, qubits = qml.qchem.molecular_hamiltonian(symbols, coordinates)
print("Number of qubits = ", qubits)
print("The Hamiltonian is ", H)

# Implementing the VQE
dev = qml.device("lightning.qubit", wires=qubits)
electrons = 2
hf = qml.qchem.hf_state(electrons, qubits)
print(hf)