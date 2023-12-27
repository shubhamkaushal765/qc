# qc - Quantum Computing

### hello_world.py
- run basic circuit on local simulators. (testing both ideal and noisy)
- qubits are by default initialized to |0>

### test_statevectors.py
- Transpilation: is the process of writing the input circuit to match the topology of specific quantum device, and/or to optimize the circuit for present day noisy qc.
- Don't put any measurements on the circuit. Measurements will lead to a collapse of the qubits, and we won't get the state of the qubits at that poistion in the circuit.

### IBMsinglequantumsystem.py
- Testing state vectors, single qubit operatons.

### quantumteleportation.py
- Teleportation circuit completed successfully.
- Add barriers, take q to be definitely measurable (e.g. 0/1 state), apply random UnitaryGate to get a random quantum state.
- Apply the inverse of the unitaryGate on B and measure. It will be definitive. (0/1 state)
- Complete implementation of bell states' circuit.