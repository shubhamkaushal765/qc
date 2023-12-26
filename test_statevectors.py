from qiskit import transpile, assemble, Aer, QuantumCircuit

# circuit
circuit = QuantumCircuit(2)  # default to |0>
circuit.h(0)
circuit.cx(0, 1)
print(circuit.draw())

# statevector simulator
svsim = Aer.get_backend('statevector_simulator')
test = transpile(circuit, svsim)
qobj = assemble(test)
statevectors = svsim.run(circuit).result().get_statevector()
print(statevectors)

