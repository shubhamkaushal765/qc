# qc - Quantum Computing

## quantumteleportation.py

- `Quantum teleportation` is a protocol where a sender transmits a qubit to a receiver by making use of a shared entangled quantum state along with two bits of classical communication.
- The entanglement is lost in the process.

## Circuit
```
            ┌─────────────────────┐            ┌───┐ ░ ┌─┐    ░
q3_0: ──────┤ Initialize(0.6,0.8) ├─────────■──┤ H ├─░─┤M├────░───────■─
      ┌─────┴─────────────────────┴──────┐┌─┴─┐└───┘ ░ └╥┘┌─┐ ░       │
q3_1: ┤0                                 ├┤ X ├──────░──╫─┤M├─░───■───┼─
      │  Initialize(0.70711,0,0,0.70711) │└───┘      ░  ║ └╥┘ ░ ┌─┴─┐ │
q3_2: ┤1                                 ├───────────░──╫──╫──░─┤ X ├─■─
      └──────────────────────────────────┘           ░  ║  ║  ░ └───┘
c0: 2/══════════════════════════════════════════════════╩══╩════════════
                                                        0  1
```
## Bell States

$$
|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$
$$
|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)
$$
$$
|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle)
$$
$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)
$$

