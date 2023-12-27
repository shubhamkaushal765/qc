from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, transpile
from qiskit.quantum_info import Statevector
import numpy as np

def get_bell_state(state='phi+'):

    assert state in ['phi+', 'phi-', 'psi+', 'psi-']

    ##### TODO: add from_circuit to the function argument after completing modifying the circuit.
    from_circuit = False
    if not from_circuit:
        if state == 'phi+':
            return Statevector([1./np.sqrt(2), 0, 0, 1./np.sqrt(2)])
        elif state == 'phi-':
            return Statevector([1./np.sqrt(2), 0, 0, -1./np.sqrt(2)])
        elif state == 'psi+':
            return Statevector([0, 1./np.sqrt(2), 1./np.sqrt(2), 0])
        elif state == 'psi+':
            return Statevector([0, 1./np.sqrt(2), -1./np.sqrt(2), 0])

    # preparing an entangled state
    ##### TODO: modify circuit for different bell states
    ## circuit
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)

    ## qubits as state vectors
    svsim = Aer.get_backend("statevector_simulator")
    job_sv = svsim.run(transpile(circuit, svsim), shots=100)
    results = job_sv.result()
    statevector = results.get_statevector()
    print(statevector)
    return statevector

def teleportation_circuit(q, ab):
    qr = QuantumRegister(3) # Q, A, B
    cr = ClassicalRegister(2)

    qc = QuantumCircuit(qr, cr)
    qc.initialize(q, [0]) # q
    qc.initialize(ab, [1, 2]) # a, b

    qc.cnot(qr[0], qr[1])
    qc.h(qr[0])

    qc.measure(qr[0], cr[0])
    qc.measure(qr[1], cr[1])

    qc.cx(qr[1], qr[2])
    qc.cz(qr[0], qr[2])

    return qc


if __name__ == "__main__":
    ab_statevector = get_bell_state(state='phi+')

    # qubit to teleport
    qbit_2_teleport = Statevector([3/5, 4/5])
    print(qbit_2_teleport.is_valid())

    # define teleportation circuit
    qc = teleportation_circuit(qbit_2_teleport, ab_statevector)
    print(qc)

    # run simulation
    print(qbit_2_teleport)
    svsim = Aer.get_backend("statevector_simulator")
    jobs_teleportation = svsim.run(transpile(qc, svsim), shots=100)
    results = jobs_teleportation.result()
    print(results.get_statevector())
