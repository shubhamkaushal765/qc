# Quantum Neural Network - Qiskit

The motivation behind **quantum machine learning (QML)** is to integrate notions from quantum computing and classical machine learning to open the way for new and improved learning schemes. QNNs apply this generic principle by combining classical neural networks and parametrized quantum circuits. Because they lie at an intersection between two fields, QNNs can be viewed from two perspectives:

From a **machine learning** perspective, QNNs are, once again, algorithmic models that can be trained to find hidden patterns in data in a similar manner to their classical counterparts. These models can load classical data (inputs) into a quantum state, and later process it with quantum gates parametrized by trainable weights. Figure 1 shows a generic QNN example including the data loading and processing steps. The output from measuring this state can then be plugged into a loss function to train the weights through backpropagation.

From a **quantum computing** perspective, QNNs are quantum algorithms based on parametrized quantum circuits that can be trained in a variational manner using classical optimizers. These circuits contain a feature map (with input parameters) and an ansatz (with trainable weights).

![](images/qiskit_qnn.jpg)

### `day22 - QNN with Qiskit.ipynb`

> Exploring `EstimatorQNN` and `SamplerQNN`

In qiskit-machine-learning module from Qiskit, `EstimatorQNN` and `SamplerQNN` are two specific types of quantum neural networks provided by the module.

`EstimatorQNN` is a type of quantum neural network designed for supervised learning tasks, particularly regression problems. It is implemented in the `qiskit_machine_learning.neural_networks.EstimatorQNN` class. This QNN combines a parameterized quantum circuit with a classical neural network to approximate a target function or predict a continuous output value based on input data.
On the other hand, `SamplerQNN` is a type of quantum neural network designed for generative tasks, such as sampling from complex probability distributions. It is implemented in the `qiskit_machine_learning.neural_networks.SamplerQNN` class. This QNN uses a parameterized quantum circuit to encode a probability distribution over the output space, and during inference, it generates samples from this distribution by measuring the quantum circuit multiple times.

Both `EstimatorQNN` and `SamplerQNN` in the qiskit-machine-learning module leverage the hybrid quantum-classical architecture, where a quantum circuit is combined with classical neural network components. The quantum circuits in these QNNs are parameterized, and the parameters are optimized during the training process using classical optimization techniques.