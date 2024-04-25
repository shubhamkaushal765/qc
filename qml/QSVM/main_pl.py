import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import pennylane as qml


class QSVM_PENNYLANE:
    """
    This class implements a QSVM model using PennyLane for quantum circuit computations.
    """

    def __init__(self):
        """
        Initializes the QSVM_PENNYLANE model.
        The number of qubits (wires) is determined dynamically based on the dataset size and encoding type.
        """

        # Dataset variables
        self.x_tr = None
        self.x_test = None
        self.y_tr = None
        self.y_test = None

        # Device variables
        self.wires = None
        self.dev = None

        # Kernel variables
        self.qkernel = None

    def configure_dataset(self, reduce_dims_to=None):
        """
        Configures the dataset for training and testing.

        This method loads the Wine dataset, preprocesses it, and optionally reduces its dimensionality using PCA.

        Args:
            reduce_dims_to (int): Number of dimensions to reduce the dataset to using PCA.

        Returns:
            None
        """

        # Load the Wine dataset
        x, y = load_wine(return_X_y=True)
        x = x[: 59 + 71]
        y = y[: 59 + 71]

        # Split the dataset into train and test sets
        x_tr, x_test, y_tr, y_test = train_test_split(x, y, train_size=0.9)

        # Normalize the dataset
        scaler = MaxAbsScaler()
        x_tr = scaler.fit_transform(x_tr)
        x_test = scaler.transform(x_test)
        x_test = np.clip(x_test, 0, 1)

        # Optionally reduce dimensions using PCA
        if reduce_dims_to:
            pca = PCA(n_components=reduce_dims_to)
            x_tr = pca.fit_transform(x_tr)
            x_test = pca.transform(x_test)

        self.x_tr = x_tr
        self.x_test = x_test
        self.y_tr = y_tr
        self.y_test = y_test

    def configure_kernel(self, enc_type="amplitude", device="lightning.qubit"):
        """
        Configures the quantum kernel circuit.

        This method sets up the quantum kernel circuit based on the chosen encoding type and device.

        Args:
            enc_type (str): Type of encoding to use for quantum data embedding. Can be 'amplitude' or 'angle'.
            device (str): PennyLane device to use for quantum computations.

        Returns:
            None
        """

        assert enc_type in ["amplitude", "angle"], "Encoding type not supported."

        # Determine the number of qubits required based on the dataset size and encoding type
        wires = len(self.x_tr[0])
        if enc_type == "amplitude":
            wires = np.ceil(np.log2(wires)).astype(int)
        self.wires = wires
        self.dev = qml.device(device, wires=self.wires)

        print(f"Number of cols: {len(self.x_tr[0])}, Wires: {wires}")

        @qml.qnode(self.dev)
        def kernel_circuit(a, b):
            # Quantum data embedding based on the chosen encoding type
            if enc_type == "amplitude":
                qml.AmplitudeEmbedding(
                    a, wires=range(self.wires), pad_with=0, normalize=True
                )
                qml.adjoint(
                    qml.AmplitudeEmbedding(
                        b, wires=range(self.wires), pad_with=0, normalize=True
                    )
                )
            if enc_type == "angle":
                qml.AngleEmbedding(a, wires=range(self.wires))
                qml.adjoint(qml.AngleEmbedding(b, wires=range(self.wires)))

            # the state is phi(b)^T . phi(a) . |0>
            # if a == b, then qml.probs should be == 1
            # Calculate the inner product of the embedded quantum data
            return qml.probs(wires=range(self.wires))

        def qkernel(A, B):
            return np.array([[kernel_circuit(a, b)[0] for b in B] for a in A])

        self.qkernel = qkernel

    def train_svc(self):
        """
        Trains the support vector machine (SVM) using the configured QSVM kernel.

        This method trains an SVM classifier using the quantum kernel defined earlier.

        Returns:
            None
        """

        svm = SVC(kernel=self.qkernel).fit(self.x_tr, self.y_tr)
        print("Accuracy:", accuracy_score(svm.predict(self.x_test), self.y_test))


if __name__ == "__main__":
    qsvm_pl = QSVM_PENNYLANE()  # Initialize QSVM_PENNYLANE
    qsvm_pl.configure_dataset(reduce_dims_to=8)  # Configure the dataset
    qsvm_pl.configure_kernel(enc_type="angle")  # Configure the quantum kernel
    qsvm_pl.train_svc()  # Train the SVM
