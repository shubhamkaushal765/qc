import cirq
import random


def get_deutsch_fn():
    """
    Deutsch Algorithm function.

    Returns:
    callable: An oracle function that takes no arguments and returns 0 or 1.
    """
    return [random.randint(0, 1) for _ in range(2)]


def main():
    q0, q1 = cirq.LineQubit.range(2)
    deutsch_fn = get_deutsch_fn()

    print(f"Deutsch Function: {deutsch_fn}")

    # preparing the initial qubits.
    init = cirq.Circuit(
        cirq.H(q0),
        cirq.X(q1),
        cirq.H(q1),
    )

    # Unitary oracle gates
    if deutsch_fn[0] == deutsch_fn[1] and deutsch_fn[0] == 0:
        middle = cirq.Circuit()
    elif deutsch_fn[0] == deutsch_fn[1] and deutsch_fn[0] == 1:
        middle = cirq.Circuit(
            cirq.X(q1),
        )
    elif deutsch_fn[0] != deutsch_fn[1]:
        middle = cirq.Circuit(
            cirq.CX(q0, q1),
        )

    # Measurements
    end = cirq.Circuit(
        cirq.H(q0),
        cirq.measure(q0, key="Constant-Balanced"),
    )

    circuit = init + middle + end
    print(circuit)

    print(f"Simulating the circuit...")
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=10)
    print(result)
    print("########################")


if __name__ == "__main__":
    for i in range(10):
        main()
