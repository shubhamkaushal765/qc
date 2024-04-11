import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import docplex model to generate the problem to optimize
from docplex.mp.model import Model

# Import the libraries needed to employ the QAOA quantum algorithm using OpenQAOA
from openqaoa import QAOA

# method to covnert a docplex model to a qubo problem
from openqaoa.problems.converters import FromDocplex2IsingModel
from openqaoa.backends import create_device

# method to find the corrects states for the QAOA boject
from openqaoa.utilities import ground_state_hamiltonian

values = [3, 6, 3, 4, 5]
weights = [3, 5, 6, 2, 4]
max_weight = 13
