from cmath import exp, inf, pi, sqrt, cos, sin
from multiprocessing.sharedctypes import Value
from tracemalloc import start, stop
from scipy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve
from numpy.linalg import norm, inv, eig

# Task 1

A = np.random.randint(2, size=(3, 3))
M = np.tril(A) + np.tril(A, -1).T
print(M)
E = eig(M)[1]
print(E)
for r in E:
    for c in E:
        print(r)
        print(c)
        if(np.dot(r, c) != 0):
            print("False")
