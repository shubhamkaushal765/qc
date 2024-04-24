- QAOAKit build fails from `pip install QAOAKit`; install from source on GitHub.
  - failing on windows system.
  - Tried on WSL: installed the package in chunks
    ```bash
    pip install qiskit==1.0.2 qiskit-aer==0.13.3 scikit-learn==1.4.1.post1 pynauty==1.1.2
    pip install qiskit-opmitization numpy pandas networkx pytest tqdm cvxgraphalgs cvxopt notebook matplotlib seaborn
    pip install --no-deps QAOAKit
    ```
    - Fix the imports in the QAOAKit module to the current version of Qiskit:
    ```bash
    qaoa.py:line4:from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    utils.py:line9:from qiskit_aer import AerSimulator
    ```

- Set `requirements.txt`

    ```bash
    pip install pipreqs
    pipreqs --force --ignore "_env_qc, QAOAKit, __pycache__" .
    ```