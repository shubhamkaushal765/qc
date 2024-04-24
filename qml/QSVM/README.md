# QSVM_PENNYLANE

This repository contains a QSVM (Quantum Support Vector Machine) implementation using PennyLane for quantum circuit computations.

## Overview

This QSVM model is designed to work with the Wine dataset. It utilizes PennyLane for quantum computations and scikit-learn for classical machine learning tasks.

## Installation

To run this code, you need Python 3.x along with the following libraries:
- numpy
- scikit-learn
- PennyLane

You can install the required libraries using pip:

```bash
pip install numpy scikit-learn pennylane
```

## Configuration

### Dataset

The Wine dataset is used for training and testing the QSVM model. The dataset is preprocessed and optionally reduced in dimensionality using PCA.

### Quantum Kernel

The quantum kernel circuit is configured based on the chosen encoding type and device. Currently, two encoding types are supported: amplitude and angle.

### Training

The QSVM_PENNYLANE model is trained using the configured SVM classifier and quantum kernel.

## Example

```python
from QSVM_PENNYLANE import QSVM_PENNYLANE

qsvm_pl = QSVM_PENNYLANE()  # Initialize QSVM_PENNYLANE
qsvm_pl.configure_dataset(reduce_dims_to=8)  # Configure the dataset
qsvm_pl.configure_kernel(enc_type="angle")  # Configure the quantum kernel
qsvm_pl.train_svc()  # Train the SVM
```

## Results

The following are the results obtained with different configurations:

| Data Reduction    | Encoding  | Wires | Accuracy |
| ----------------- | --------- | ----- | -------- |
| No reduction (13) | Amplitude | 4     | 0.9231   |
| Reduction to 8    | Amplitude | 3     | 0.6923   |
| Reduction to 8    | Angle     | 8     | 1.0      |

### Insights

- **Amplitude Encoding vs. Angle Encoding**: When comparing the performance of amplitude encoding and angle encoding, we observe that angle encoding achieved perfect accuracy (1.0) when the data was reduced to 8 dimensions, while amplitude encoding showed a significant decrease in accuracy from 0.9231 to 0.6923. This indicates that angle encoding might be more effective in capturing the underlying structure of the reduced-dimensional dataset.

- **Impact of Data Reduction**: Dimensionality reduction to 8 dimensions had a notable impact on the model's performance, particularly when using amplitude encoding. The accuracy dropped by around 23% when compared to the scenario with no reduction. However, angle encoding showcased robustness to dimensionality reduction, maintaining a high accuracy rate of 1.0. This suggests that angle encoding might be a preferable choice when dealing with reduced-dimensional datasets, as it retains more relevant information for classification.
