# qc - Quantum Computing

## Algorithms

`BRANCH: algorithms`

### Query model

| input | f_0 | f_1 | f_2 | f_3 |
|-------|-----|-----|-----|-----|
|   0   |  0  |  0  |  1  |  1  |
|   1   |  0  |  1  |  0  |  1  |

- First and last are constant functions, the inner two are balanced functions.
- constants are non-unitary. So, it can't be simulated using quantum circuits.
- Hence, defining a reversible function with a CX gate with control on f.

```
           ┌───┐
q2_0: -----┤ f ├
           └───┘
           ┌─┴─┐
q2_1: ─────┤ X ├
           └───┘
```

---

## Other Branches

### quantumteleportation.py

`BRANCH: quantum_teleporatation:`

- Teleportation circuit completed successfully.
- Add barriers, take q to be definitely measurable (e.g. 0/1 state), apply random UnitaryGate to get a random quantum state.
- Apply the inverse of the unitaryGate on B and measure. It will be definitive. (0/1 state)
- Complete implementation of bell states' circuit.

### superdense_coding.py

`BRANCH: superdense_coding`

- send two classical bits using one qubit (at a cost of one e-bit of entanglement)
- `Holevo's Theorom` : Quantum Information Theory: Without the use of entanglement, it is impossible to send more than one bit of information using a single qubit.
