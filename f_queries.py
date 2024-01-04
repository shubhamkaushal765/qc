from qiskit import QuantumCircuit, QuantumRegister

def f_func(function_index=0):
    # There are only four valid functions for a single qubit circuit.
    f = {
        0: (0, 0),
        1: (0, 1),
        2: (1, 0),
        3: (1, 1),
    }
    return f[function_index]

def reversible_function(function_index=0):
    qbits = QuantumRegister(2)
    circuit = QuantumCircuit(qbits)

    if function_index == 0:
        pass
    elif function_index == 1:
        circuit.cx(qbits[0], qbits[1])
    elif function_index == 2:
        circuit.x(qbits[0])
        circuit.cx(qbits[0], qbits[1])
    elif function_index == 3:
        circuit.x(qbits[1])
        circuit.x(qbits[0])
    
    print(circuit.draw())
    return f_func(function_index), qbits, circuit

if __name__ == "__main__":
    for i in range(4):
        reversible_function(i)