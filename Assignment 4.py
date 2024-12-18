from cmath import exp, inf, pi, sqrt, cos, sin
from multiprocessing.sharedctypes import Value
from re import A
from tracemalloc import start, stop
import matplotlib
from scipy import *
import matplotlib.pyplot as plt
import sys
import numpy as np

# Task 1

def f(phi, r):
    return r * exp(1j * phi)

phi = [i for i in np.linspace(0, 2*pi)]
r = [i for i in np.linspace(0.1, 1)]
for i in r:
    for k in phi:
        plt.plot(f(k, i).real, f(k, i).imag, 'o')
plt.show()


# Task 2

def newton(f, fp, x, tol):
    i = 0
    while(abs((x - f(x)/fp(x)) - x) > tol and i < 1000):
        x = x - f(x)/fp(x)
        i += 1
    if (i >= 400):
        conv = False
    else:
        conv = True
    return x, conv, i

def f(x):
    return np.sin(x) - np.cos(4*x)
def fp(x):
    return np.cos(x) + 4*np.cos(4*x)

print(newton(f, fp, 0, 1.e-18))