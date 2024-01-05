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

### Shor's Algorithm

Three parts to the computation:
- Converting the factoring problem to period finding
- Find the period using QFT
- Find the factors using the period.

The logic:

- find period x^r = 1 mod N: r is the period, N is the number to factor.
- Let N = pq, where p, q are prime numbers
- Period Finding
    - pick x at random from (1, N)
    - if gcd(x, N) != 1, then p or q must be that gcd.
    - else x and N must be coprimes. Find r (the period).
    - repeat for different values of x.
- x^r = 1 mod N => x^r - 1 = 0
- If r is even, then it can be split into two factors, which must be some mulitples of p and q.

```
# testing the classical version
# code in shor.py
# Output of the code
Starting Classical Shor's algorithm...
To Factor, N: 8633
Base, X: 1715,
Exponent, R: 528
The factors are: 89, 97.
================================================
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
