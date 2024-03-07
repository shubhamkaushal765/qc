import numpy as np

# qiskit imports
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit import BasicAer
from qiskit import execute

# generating random theta to measure
theta = np.random.randn()
print(f"Theta: {theta}")

# circuit to perform rotation
q = QuantumRegister(3)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

# GHZ State
qc.h(q[0])
qc.cx(q[0],q[1])
qc.cx(q[0],q[2])
qc.rz(theta,q[0])
qc.rz(theta,q[1])
qc.rz(theta,q[2])
qc.cx(q[0],q[2])
qc.cx(q[0],q[1])
qc.h(q[0])
qc.measure(q[0],c)
print(qc)
################################

backend = BasicAer.get_backend("qasm_simulator")
job = execute(qc, backend, shots=1024)
result = job.result().get_counts(qc)
print(result)
################################

print(np.cos(theta/2) ** 2)
print(np.sin(theta/2) ** 2)

