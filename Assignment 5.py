from cmath import exp, inf, pi, sqrt, cos, sin
from multiprocessing.sharedctypes import Value
from re import A
from tracemalloc import start, stop
from scipy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve

# Task 1

omega = 2 * pi

def f(x):
    return np.sin(omega * x)

print(quad(f, 0, pi/2))


# Task 2

o = np.linspace(0, 2*pi, 1000)

for omega in o:
    plt.plot(omega, quad(f, 0, pi/2)[0], '.')
plt.xlabel('Omega')
plt.ylabel('Quad value')
plt.title('Integration')
plt.show()


# Task 3

def p(x):
    return x**2 + x - 3
print(fsolve(p, 2))


# Task 4

def p(x):
    return a*x**2 + x - 3

for a in np.linspace(1,5):
    plt.plot(a, fsolve(p, 2), '.')
plt.show()