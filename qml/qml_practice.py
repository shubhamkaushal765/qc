from qiskit.quantum_info import Statevector

n = 3
psi = Statevector.from_int(4, dims=2**n)
psi.draw("latex")
print(psi)