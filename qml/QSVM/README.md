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
