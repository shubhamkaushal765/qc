import cirq
import random


def main(n_qubits=4):

    # input sanitization
    assert (
        n_qubits % 2 == 0
    ), f"Balanced only allowed for even number of qubits, input given: {n_qubits} qubits."
    assert n_qubits > 1, "Trivial for 1 qubit."

    # inititalize with one extra qubit
    q = cirq.LineQubit.range(n_qubits + 1)

    # some example oracle functions
    constant = ([], [cirq.X(q[n_qubits])])
    b_0 = [[cirq.CNOT(q[i], q[n_qubits])] for i in range(n_qubits)]
    b_1 = [b_0_i + [cirq.X(q[n_qubits])] for b_0_i in b_0]
    balanced = b_0 + b_1

    # choose a random function
    oracle_function = None
    choice = random.randint(0, 1)
    if choice == 0:
        print("Function chosen is constant!", end=" ")
        oracle_function = random.choice(constant)
    elif choice == 1:
        print("Function chosen is balanced!", end=" ")
        oracle_function = random.choice(balanced)

    # circuit init + last-qubit in |-> state
    init = cirq.Circuit(cirq.H(q[i]) for i in range(n_qubits)) + cirq.Circuit(
        cirq.X(q[n_qubits]), cirq.H(q[n_qubits])
    )

    # interference + measurement
    interference = cirq.Circuit(cirq.H(q[i]) for i in range(n_qubits))
    measurement = cirq.measure(q[0:n_qubits])

    # final circuit
    circuit = init + oracle_function + interference + measurement

    # simulate
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1)
    vals = [i for i in result.measurements.values()][0][0]
    print("Measurement Results: ", "".join(map(str, vals)))


if __name__ == "__main__":
    for i in range(10):
        main()
