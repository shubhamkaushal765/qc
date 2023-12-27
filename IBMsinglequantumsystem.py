from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# definfing statevectors and experimenting
# v = Statevector([3/5, 4j/5])
# print(v.draw())
# print(v.is_valid())

# statistics = v.sample_counts(1000)
# print(statistics)
# plt.bar(statistics.keys(), statistics.values(), width=1, color='g')
# plt.show()

# definfing circuit and evolving a state vector
from qiskit import QuantumCircuit

circuit =  QuantumCircuit(1)
circuit.h(0)
circuit.x(0)
circuit.t(0)
circuit.h(0)

ket1 = Statevector([0, 1])
v = ket1.evolve(circuit)
print(v.draw())
print(circuit.draw())
stats = v.sample_counts(1000)
plt.bar(stats.keys(), stats.values(), width=1, color='g')
plt.show()