from math import log
import numpy as np
import matplotlib.pyplot as plt

labels = [
    "Constant"
    "Logaritimic"
    "Linear"
    "Log linear"
    "Quadratic"
    "Cubic"
    "Exponential"
    ]

big_o = [np.ones(n.shape), np.log(n),n, n * np.log(n), n**2, n**3, 2**n]