from cmath import exp, inf, pi, sqrt, cos, sin
from multiprocessing.sharedctypes import Value
from tracemalloc import start, stop
from scipy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve
from numpy.linalg import norm, inv

# Task 1

def isSymmetric(M):
    if (np.array_equal(M, M.transpose())):
        return 1
    elif(np.array_equal(M, -M.transpose())):
        return -1
    else:
        return 0

M = np.array([[0, 2, -3], [-2, 0, -4], [3, 4, 0]])
print(M)
print(isSymmetric(M))


# Task 2

def isOrtho(a1, a2):
    return np.dot(a1, a2) == 0
a1 = np.array([1, 0, 0])
a2 = np.array([0, 1, 0])
print(isOrtho(a1, a2))


# Task 3

A = np.array([[1, 1], [1, 1]])
print(A)

def normed(A):
    sum = 0
    for a in A:
        sum += a
    return A/sqrt(np.abs(sum))
print(normed(A))
print(A/np.sqrt(norm(A)))


# Task 4
x = 0
A = np.array([[np.cos(x), np.sin(x)], [-np.sin(x), np.cos(x)]])
B = inv(A)
print(A*B)
print(A.transpose())