from cmath import inf, sqrt
from multiprocessing.sharedctypes import Value
from re import A
from tracemalloc import start, stop
import matplotlib
from scipy import *
from matplotlib.pyplot import *
import sys
import numpy

# Task 4

distance = [[0, 20, 30, 40],
            [20, 0, 50, 60],
            [30, 50, 0, 70],
            [40, 60, 70, 0]]
print(distance)

redDistance = [distance[i][i+1:4] for i in range(3)]

print(redDistance)

print(numpy.tril(distance))


# Task 5

def symDif(A, B):
    diffA = A.difference(B)
    diffB = B.difference(A)
    return diffA.union(diffB)


A = {1, 3, 5, 7, 9}
B = {1, 3, 5, 7}
print(symDif(A, B))
print(A.symmetric_difference(B))


# Task 6

A.intersection_update(B)
print(A)


# Task 8

def f(x):
    return 3 * x ** 2 - 5


def bisec(a, b, tol):
    while(b - a > tol):
        if (f(a) * f((a + b) / 2) < 0):
            b = (a + b) / 2
        elif (f((a+b)/2)*f(b) < 0):
         a = (a + b) / 2
    return a, b, (a + b) / 2
print(bisec(-1.5, -0.4, 1.e-4))
    