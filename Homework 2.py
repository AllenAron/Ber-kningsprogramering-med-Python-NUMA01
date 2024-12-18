from cmath import exp, inf, pi, sqrt, cos, sin
import imghdr
from mimetypes import init
from multiprocessing.sharedctypes import Value
from re import I
from tracemalloc import start, stop
from scipy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve
from numpy.linalg import norm, inv, eig

# Task 1

class Interval:
    def __init__(self, min, *max):
        if len(max) == 0:
            self.intmin = min
            self.intmax = min
        else:
            self.intmin = min
            self.intmax = max[0]
        
    def __add__(self, I):
        if(not isinstance(I, Interval)):
            return Interval(self.intmin + I, self.intmax + I)
        else:
            return Interval(self.intmin + I.intmin, self.intmin + I.intmax)

    def __radd__(self, nbr):
        return Interval(self.intmin + nbr, self.intmax + nbr)

    def __sub__(self, I):
        if(not isinstance(I, Interval)):
            return Interval(self.intmin - I, self.intmax - I)
        else:
            return Interval(self.intmin - I.intmax, self.intmax - I.intmin)
    
    def __rsub__(self, nbr):
        return Interval(nbr - self.intmax, nbr - self.intmin)

    def __mul__(self, I):
        # [a, b] * [c, d] = [min(ac, ad, bc, bd), max(ac, ad, bc, bd)]
        if(not isinstance(I, Interval)):
            lmin = min(self.intmin * I, self.intmin * I, self.intmax * I, self.intmax * I)
            lmax = max(self.intmin * I, self.intmin * I, self.intmax * I, self.intmax * I)
        else:
            lmin = min(self.intmin * I.intmin, self.intmin * I.intmax, self.intmax * I.intmin, self.intmax * I.intmax)
            lmax = max(self.intmin * I.intmin, self.intmin * I.intmax, self.intmax * I.intmin, self.intmax * I.intmax)
        return Interval(lmin, lmax)
        
    def __rmul__(self, nbr):
        lmin = min(self.intmin * nbr, self.intmin * nbr, self.intmax * nbr, self.intmax * nbr)
        lmax = max(self.intmin * nbr, self.intmin * nbr, self.intmax * nbr, self.intmax * nbr)
        return Interval(lmin, lmax)

    def __truediv__(self, I):
        # [a, b] / [c, d] = [min(a/c, a/d, b/c, b/d), max(a/c, a/d, b/c, b/d)], 0 /∈[c, d]
        if (np.abs(I.intmin) > 1.e-4 and np.abs(I.intmax) > 1.e-4):
            lmin = min(self.intmin / I.intmin, self.intmin / I.intmax, self.intmax / I.intmin, self.intmax / I.intmax)
            lmax = max(self.intmin / I.intmin, self.intmin / I.intmax, self.intmax / I.intmin, self.intmax / I.intmax)
            return Interval(lmin, lmax)
        else:
            raise Exception("ZeroDivisionError: division by zero")

    def __pow__(self, n):
        if(n % 2 == 0):
            if(self.intmin >= 0):
                return Interval(self.intmin**n, self.intmax**n)
            elif(self.intmax < 0):
                return Interval(self.intmax**n, self.intmin**n)
            else:
                return Interval(0, max(self.intmin**n, self.intmax**n))
        else:
            return Interval(self.intmin**n, self.intmax**n)
    
    def __contains__(self, val):
        if (val <= self.intmax and val >= self.intmin):
            return True
        else:
            return False
    
    def __neg__(self):
        return Interval(-self.intmax, -self.intmin)

    def __repr__(self):
            return f"[{self.intmin}, {self.intmax}]"
    
    def getMax(self):
        return self.intmax
    
    def getMin(self):
        return self.intmin
    
I1 = Interval(1, 4)
I2 = Interval(-2, -1)
print(I1)
I3 = I1 / I2
print(I3)
I4 = Interval(2, 3) + 1.0
print(I4)
I5 = -Interval(2, 3)
I6 = Interval(-2, 2)
print(I5)
print((I6**3))


# Task 10

xl = np.linspace(0, 1, 1000)
intlist = []
plist = []

for l in xl:
    intlist.append(Interval(l, l + 0.5))

def p(I):
    return 3*I**3 - 2*I**2 - 5*I - 1

for I in intlist:
    plist.append(p(I))

for i in range(xl.__len__()):
    plt.plot(xl[i], plist[i].getMin(), '.')
    plt.plot(xl[i], plist[i].getMax(), '.')
plt.show()

print(p(I1))
I7 = p(I1)
print(I7.getMin())