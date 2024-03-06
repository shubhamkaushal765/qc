import cirq
import numpy as np


def C_U_gate(circuit, angle, qubits, ancilla):
    """
    Construct a controlled unitary gate in the given circuit.

    Parameters:
    - circuit (cirq.Circuit): The quantum circuit to which the gate is added.
    - angle (float): The angle for the unitary gate.
    - control_qubits (List[cirq.QubitId]): List of control qubits.
    - ancilla_qubit (cirq.QubitId): Ancilla qubit.

    Returns:
    cirq.Circuit: The modified quantum circuit with the added controlled unitary gate.
    """
    gate = cirq.MatrixGate(
        matrix=np.array([[np.exp(2 * np.pi * 1.0j * angle), 0], [0, 1]])
    )
    for i in range(len(qubits)):
        circuit += [gate.on(ancilla).controlled_by(qubits[i]) ** (2**i)]
    return circuit


def qpe(angle=0.75, n_qubits=2, repetitions=1):
    """
    Perform Quantum Phase Estimation (QPE) for a given angle and number of qubits.

    Parameters:
    - angle (float): The angle for the controlled unitary gate.
    - n_qubits (int): The number of qubits used in the QPE.
    - repetitions (int): The number of times to repeat the QPE circuit.

    Returns:
    cirq.Result: The result of the QPE circuit.
    """

    # initialize the qubits
    ancilla = cirq.LineQubit(-1)
    q = cirq.LineQubit.range(n_qubits)
    circuit = cirq.Circuit([cirq.H(q_i) for q_i in q])

    # controlled-U operation
    circuit = C_U_gate(circuit, angle, q, ancilla)

    # adding inverse QFT to the circuit
    circuit.append(cirq.qft(*q, without_reverse=True, inverse=True))

    # measurement
    circuit.append(cirq.measure(*q, key="phase"))

    # print(circuit)

    # gather results
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=repetitions)
    return result


if __name__ == "__main__":
    repetitions = 100

    for n_qubits in (2, 4, 8, 16):
        print(f"Testing with {n_qubits} qubits.")
        errors = []
        
        for angle in np.arange(0, 1, 0.1):
            result = qpe(angle, n_qubits, repetitions=repetitions)
            mode = result.data["phase"].mode()[0]
            guess = mode / 2**n_qubits
            print(f"target: {angle:0.4f}, estimiate: {guess:0.4f}={mode}/{2**n_qubits}")
            errors.append((angle - guess) ** 2)
            
        rms = np.sqrt(sum(errors) / len(errors))
        print(f"RMS Error: {rms: 0.4f}")
