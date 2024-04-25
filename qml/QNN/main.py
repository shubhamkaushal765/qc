from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
from sklearn.decomposition import PCA

import pennylane as qml
from pennylane import numpy as np

from itertools import combinations


class QNN_PENNYLANE:
    def __init__(self):
        pass

    def configure_dataset(self, reduce_dimension_to=None):

        x, y = load_breast_cancer(return_X_y=True)
        x_tr, x_test, y_tr, y_test = train_test_split(x, y, train_size=0.8)
        x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, train_size=0.5)

        scaler = MaxAbsScaler()
        x_tr = scaler.fit_transform(x_tr)
        x_test = scaler.transform(x_test)
        x_val = scaler.transform(x_val)

        # Restrict all the values to be between 0 and 1.
        x_test = np.clip(x_test, 0, 1)
        x_val = np.clip(x_val, 0, 1)

        if reduce_dimension_to:
            pca = PCA(n_components=reduce_dimension_to)
            x_tr = pca.fit_transform(x_tr)
            x_test = pca.transform(x_test)
            x_val = pca.transform(x_val)

        self.x_tr, self.y_tr = x_tr, y_tr
        self.x_test, self.y_test = x_test, y_test
        self.x_val, self.y_val = x_val, y_val

    def data_encoding(self, enc_type="amplitude", device="lightning.qubit"):
        """
        Total: 30 columns
        1. Amplitude encoding: 5 qubits
        2. Any other encoding with dimensionality reduction
        """

        ncols = len(self.x_tr[0])

        if enc_type == "amplitude":
            wires = np.ceil(np.log2(ncols)).astype(int)
            print(wires)
            self.dev = qml.device(device, wires=wires)

    def ZZFeatureMap(self, nqubits, data):
        nload = min(len(data), nqubits)

        for i in range(nload):
            qml.Hadamard(wires=i)
            qml.RZ(2 * data[i], wires=i)

        for pair in list(combinations(range(nload), 2)):
            q0 = pair[0]
            q1 = pair[1]
            qml.CZ(wires=[q0, q1])
            qml.RZ(2.0 * (np.pi - data[q0]) * (np.pi - data[q1]), wires=q1)
            qml.CZ(wires=[q0, q1])

    def TwoLocalVariationalForm(self, nqubits, theta, reps=1):
        for r in range(reps):
            for i in range(nqubits):
                qml.RY(theta[r * nqubits + i], wires=i)
            for i in range(nqubits - 1):
                qml.CNOT(wires=[i, i + 1])
            for i in range(nqubits):
                qml.RY(theta[reps * nqubits + i], wires=i)


if __name__ == "__main__":
    qnn = QNN_PENNYLANE()
    qnn.configure_dataset(reduce_dimension_to=16)
    print(qnn.x_tr[0], len(qnn.x_tr[0]))
    print(qnn.y_tr[0])
    qnn.data_encoding()

    print(qnn.dev)
    dev = qml.device("lightning.qubit", wires=4)
