import cirq
import numpy as np


class UnitaryGate(cirq.Gate):
    """
    Defines a unitary gate for quantum phase estimation.

    Parameters:
    - theta (float): Angle between 0 and 1 in radians.
    - power (int): Power of the unitary gate

    Returns:
    cirq.MatrixGate: A unitary gate.

    Notes:
    - The gate is defined as U(theta) = |1⟩⟨1| + exp(2 * π * i * theta) |0⟩⟨0|.
    """

    def __init__(self, theta, power):
        super(UnitaryGate, self)
        self.theta = theta
        self.power = power

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        gate_np = np.array([[np.exp(2 * np.pi * 1.0j * self.theta), 0], [0, 1]])
        gate_np = np.linalg.matrix_power(gate_np, self.power)
        gate = cirq.MatrixGate(matrix=gate_np)
        return gate

    def _circuit_diagram_info_(self, args):
        return f"U({self.theta})({self.power})"


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
    for i in range(len(qubits)):
        gate = UnitaryGate(angle, 2**i)
        circuit += [gate.on(ancilla).controlled_by(qubits[i])]
    return circuit


def qpe(angle=0.75, n_qubits=2, repetitions=1):

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

    print(circuit)

    # gather results
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=repetitions)
    return result


def main():
    qpe()


if __name__ == "__main__":
    main()
