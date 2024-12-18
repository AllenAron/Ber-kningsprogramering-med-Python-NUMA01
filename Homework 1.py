from cmath import sqrt, log
import matplotlib.pyplot as plt
from scipy import *
import sys
import numpy as np

# Task 1

def approx_ln(x, n):
    a = (1 + x) / 2
    g = sqrt(x)
    for i in range(n):
        a = (a + g) / 2
        g = sqrt(a * g)
    return (x - 1) / a, a

# Task 2

x = np.linspace(1, 5, 100)
for i in x:
    plt.plot(i, log(i), 'x', color = 'm')
    plt.plot(i, approx_ln(i, 20)[0], '.', color = 'b')
plt.show()


# Task 3 

n = range(1, 200)
x = 1.41
for i in n:
    plt.plot(i, abs(log(x) - approx_ln(x, i)[0]), '.', color = 'r')
plt.show()


# Task 4

def fast_approx_ln(x, n):
    d = np.zeros([n, n])
    for j in range(n):
        d[0][j] = approx_ln(x, j)[1]
        
    for i in range(n):
        for k in range(1, n):
            d[k][i] = (d[k - 1][i] - 2**(-2*k) * d[k - 1][i - 1])/(1 - 2**(-2*k))
    return ((x-1)/d[n - 1][n - 1])


# Task 5

x = np.linspace(0, 20, 200)

for x in x:
    plt.plot(x, abs(log(x) - fast_approx_ln(x, 2)), '.', color = 'r')
    plt.plot(x, abs(log(x) - fast_approx_ln(x, 3)), '.', color = 'y')
    plt.plot(x, abs(log(x) - fast_approx_ln(x, 4)), '.', color = 'g')
    plt.plot(x, abs(log(x) - fast_approx_ln(x, 5)), '.', color = 'm')

plt.legend(['2 iterations', '3 iterations', '4 iterations', '5 iterations'])
plt.yscale('log')
plt.show()