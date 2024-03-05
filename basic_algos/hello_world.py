import qiskit as q
from qiskit_aer import AerSimulator
from qiskit.providers.fake_provider import FakeManilaV2

# circuit
circuit = q.QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()
print(circuit.draw())

# ideal quantum computer simnulator
aer_ideal = AerSimulator()
result_ideal = aer_ideal.run(circuit, shots=1024).result()
counts_ideal = result_ideal.get_counts(0)
print('Counts(ideal):', counts_ideal)

# noisy quantum computer simnulator
backend = FakeManilaV2()
aer_noisy = AerSimulator.from_backend(backend)
result_noisy = aer_noisy.run(circuit, shots=1024).result()
counts_noisy = result_noisy.get_counts(0)
print('Counts(noise):', counts_noisy)

