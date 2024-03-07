import numpy as np

# qiskit imports
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit import BasicAer
from qiskit import execute

# generating random theta to measure
theta = np.random.randn()
print(f"Theta: {theta}")

# circuit to perform rotation
q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.rz(theta, q[0])
qc.h(q[0])
qc.measure(q, c)
print(qc)
################################

backend = BasicAer.get_backend("qasm_simulator")
job = execute(qc, backend, shots=1024)
result = job.result().get_counts(qc)
print(result)
################################

# TODO: Measuring entanglement

