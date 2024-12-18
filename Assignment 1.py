from cmath import sqrt
import matplotlib
from scipy import *
from matplotlib.pyplot import *
import sys
import numpy


# Task 2
def eqn(x):
    return x**2 + 0.25*x-5

print(eqn(2.3))

# Task 3
L = [1, 2]
L3 = 3*L
print(L3[-1])

# Task 4
L4 = [k**2 for k in L3]
print(L4)

# Task 5
L5 = L3 + L4
print(L5)

# Task 6
newList = [k/100 for k in range(0,101)]
print(newList)
print(len(newList))

# Task 8
xplot = []
low = 0
high = 1
length = 100
for i in range(length + 1):
    xplot.append(low + i/length)
print(xplot)
print(len(xplot))
print(type(xplot))

# Task 9
y = [numpy.arctan(k) for k in xplot]
print(y)

# Task 10
matplotlib.use("Qt5Agg")
matplotlib.pyplot.plot(xplot,y)
matplotlib.pyplot.show()

# Task 11
sum = 0
x = [k for k in range(1,201)]
value = []
for k in range(1, 201):
    sum += 1/sqrt(k)
    value.append(sum)
print(sum)
matplotlib.pyplot.plot(x, value)
matplotlib.pyplot.show()
    