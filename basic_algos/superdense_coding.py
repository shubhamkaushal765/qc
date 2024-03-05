from qiskit import QuantumRegister, QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

# SHOTS is the number of times to run the simulation
# 1 if ideal-local simulation, big number (e.g. 1024) if noisy simulation
SHOTS = 100

def superdense_coding_protocol(c, d):
    # define qubits and circuit
    qbit_A = QuantumRegister(1, 'a')
    qbit_B = QuantumRegister(1, 'b')
    protocol = QuantumCircuit(qbit_A, qbit_B)

    # entanglement
    protocol.h(qbit_A)
    protocol.cx(qbit_A, qbit_B)
    protocol.barrier()

    # superdense coding
    if d:
        protocol.z(qbit_A)
    if c:
        protocol.x(qbit_A)
    protocol.barrier()

    # the qubit A is sent to B
    # protocol on the qubits available to B (qbit_A, qbit_B)
    protocol.cx(qbit_A, qbit_B)
    protocol.h(qbit_A)
    protocol.barrier()

    # measurement
    protocol.measure_all()

    return protocol

if __name__ == "__main__":
    c, d= 1, 1
    protocol = superdense_coding_protocol(c, d)
    print(protocol)

    # simulation
    simulator = AerSimulator()
    result = simulator.run(protocol, shots=SHOTS).result()

    # get result count
    counts = result.get_counts()
    print(counts)