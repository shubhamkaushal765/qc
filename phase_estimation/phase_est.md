# Quantum Phase Estimation

> Resources: [Quantum Native Dojo](https://dojo.qulacs.org/en/latest/notebooks/2.4_phase_estimation_beginner.html), [AnonymousKet](https://anonymousket.medium.com/quantum-phase-estimation-e2910e8ef8ec), [Cirq Custom Gate](https://quantumai.google/cirq/build/custom_gates)

- Quantum Phase Estimation is used to estimate the the **eigenvalues** of a unitary matrix.

![QPE](https://miro.medium.com/v2/resize:fit:786/format:webp/1*P3CeJTp7XOrC7masXBkd1A.png)

## The Problem

$$
U|x\rangle = \lambda|x\rangle = e^{2\pi i\theta}|x\rangle
$$
where $0 \leq \theta \leq 1$, and $U$ is a unitary matrix. We would like to estimate $\theta$.

The phase $\theta$ can be written in decimal binary format as

$$
\theta = 0.\theta_1 \theta_2 \theta_3 ... \theta_n \Leftrightarrow \theta = \sum_{k=1}^{n} \theta_k 2^{-k}
$$

where each $\theta$ is either 0 or 1.

## The Algorithm

When the control-gate operation is applied, the eigenvalue information is written into the relative phase of the control qubit (like phase kickback). After the eigenvalue information is written into the relative phase, the state looks like this:

$$
\frac{{|0\rangle + e^{2\pi i 0.\theta_1}|1\rangle}}{\sqrt{2}} |\psi\rangle
$$

Applying the Hadamard gate and finding the value of $\theta_1$. if $\theta_1=0$, then H operation will give $|0\rangle$, otherwise if $\theta_1=1$ we get $|1\rangle$

$$
QFT for 0.\theta_1 \theta_2 \theta_3 ... \theta_n
$$