from cmath import inf, sqrt
from multiprocessing.sharedctypes import Value
import matplotlib
from scipy import *
from matplotlib.pyplot import *
import sys
import numpy


# Task 1

def fixedPoint(a, x):
    i = 0
    while(abs(x - (sin(x) - a * x + 30)) > 1.e-8):
        x = sin(x)-a*x+30
        i+=1
    return x

fixedPoint(0.5, 0.5)


# Task 2

x = numpy.linspace(5, 30)
value = []
a = 0.5
for k in x:
    value.append(sin(k)-a*k+30)
print(value)
matplotlib.pyplot.plot(x, value)
matplotlib.pyplot.plot(x,x)
matplotlib.pyplot.show()


# Task 3

value = []
n = 1
x = 1
while (x > 1.e-9):
    x = (sin(n)**2)/n
    n += 1
    value.append(x)
print(len(value))
matplotlib.pyplot.plot(linspace(1, 356, 355), value)
matplotlib.pyplot.show()


# Task 4, 5, 6

def sequence(a, x):
    i = 0
    negList = []
    posList = []
    while(abs(x - (0.2 * x - a * (x**2 - 5))) > 1.e-9 and i < 100):
        x = 0.2 * x - a * (x**2 - 5)
        i += 1
        if(x < 0):
            negList.append(x)
        else:
            posList.append(x)
    if(i < 30):
        return True, posList, negList
    else:
        return False, posList, negList

print(sequence(0.25, 1))