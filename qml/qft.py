import cirq
import numpy as np


class CustomQFT:
    def __init__(self, n_qubits=2):

        self.n_qubits = n_qubits
        self.circuit = None
        self.qubits = cirq.LineQubit.range(n_qubits)
        self.state_init_circuit = None
        self._set_init_circuit()
        self._get_circuit()

    def _set_init_circuit(self):
        q = self.qubits
        init_cir = cirq.Circuit()
        # for i in range(self.n_qubits):
        #     init_cir.append(cirq.H(q[i]))
        # init_cir.append(cirq.H(q[0]))
        self.state_init_circuit = init_cir

    def _get_circuit(self):

        if self.circuit is not None:
            return self.circuit

        circuit = cirq.Circuit()
        q = self.qubits
        for i in range(self.n_qubits):
            temp_cir = cirq.Circuit()
            for j in range(i):
                temp_cir.append((cirq.CZ ** (1 / 2 ** (j + 1)))(q[i], q[j]))
            circuit += temp_cir[::-1]
            circuit.append(cirq.H(q[i]))

        self.circuit = circuit
        return circuit

    def run(self):
        simulator = cirq.Simulator()
        circuit = self.state_init_circuit + self.circuit
        print(circuit)
        result = simulator.simulate(circuit)
        return np.around(result.final_state_vector, 3)


if __name__ == "__main__":
    qft = CustomQFT(n_qubits=2)
    circuit = qft._get_circuit()
    result = qft.run()
    print(result)