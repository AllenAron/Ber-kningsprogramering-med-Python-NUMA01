from cmath import exp, inf, pi, sqrt, cos, sin
import imghdr
from mimetypes import init
from multiprocessing.sharedctypes import Value
from tracemalloc import start, stop
from scipy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve
from numpy.linalg import norm, inv, eig, det

# Newtons Fractals


class fractal2D:

    def __init__(self, f, fd = None):
        self.f = f
        self.fd = fd
        self.zeroList = []
        self.tol = 1.e-12
        if fd == None:
            self.fd = self.numDeriv(f, 1.e-6)
        else:
            self.fd = fd

    def newton(self, x0):
        x = x0
        for i in range(100):
            if norm(self.f(x)) < 1.e-9:
                return x
            x = x + np.dot(inv(self.fd(x)), (-self.f(x)))
        return [-1]

    def simpNewton(self, x0):
        x = x0
        j = inv(self.fd(x))
        for i in range(100):
            if norm(self.f(x)) < 1.e-9:
                return x
            x = x + np.dot(j, (-self.f(x)))
        return [-1]

    def NewtonsMethodIt(self, xn):    
        for i in range(100):
            V = self.f(xn)
            if (np.linalg.norm(V) < 1.e-8):
                return i
            D = self.fp(xn)
            if (np.absolute(np.linalg.det(D)) < 1.e-12):
                return -1
            xn = xn - np.dot(V,(np.linalg.inv(D)))
        return -1
    
    def SimplifiedNewtonsMethodIt(self,xn):
        if (np.linalg.norm(self.f(xn)) < 1.e-12):
            return 0
        D = self.fp(xn)
        if(np.abs(D).all() < 1.e-12):
            return -1
        D = np.linalg.inv(D)
        for i in range(100):
            if (np.linalg.norm(self.f(xn)) < 1.e-12):
                return i
            xn = xn - np.dot(self.f(xn),D)
        return -1

    def getZero(self, x, boo):
        if boo == True:
            x = self.simpNewton(x)
        else:
            x = self.newton(x)
        if np.array_equal(x, [-1]):
            return -1
        for i in range(len(self.zeroList)):
            if norm(x - self.zeroList[i]) < 1.e-3:
                return i
        self.zeroList.append(x)
        return len(self.zeroList) - 1

    def plot(self, N, a, b, c, d, boo):
        A = np.linspace(a, b, N)
        B = np.linspace(c, d, N)
        G, H = np.meshgrid(A, B)
        M = np.zeros([N, N])
        for i in range(N):
            for j in range(N):
                M[i][j] = self.getZero([G[i][j], H[i][j]], boo)
        plt.pcolor(M)

    def numDeriv(self, f, h):
        def fd(x):
            x, y = x
            a, c = (f([x + h, y])-f([x, y])) / h
            b, d = (f([x + h, y])-f([x, y])) / h
            return [[a, b], [c, d]]
        return fd
    
    def itPlot(self, N, a, b, c, d, t):
        A = np.linspace(a, b, N)
        B = np.linspace(c, d, N)
        G, H = np.meshgrid(A, B)
        M = np.zeros([N, N])
        if t:
            for i in range(N):
               for j in range(N):
                  A[i,j] = self.NewtonsMethodIt(np.array([G[i,j],H[i,j]]).transpose())
        else:
            for i in range(N):
                for j in range(N):
                    A[i,j] = self.SimplifiedNewtonsMethodIt(np.array([G[i,j],H[i,j]]).transpose())
        plt.pcolor(G, H, M) 




def F(x):
    return np.array([x[0]**3 - 3*x[0]*x[1]**2 - 1, 3*x[0]**2*x[1] - x[1]**3])


def Fd(x):
    return np.array([[3*x[0]**2 - 3*x[1]**2, -6*x[0]*x[1]],
                    [9*x[0]**2*x[1], 3*x[0]**3 - 3*x[1]**2]])

frac = fractal2D(F, Fd)
frac.plot(100, -20, 20, -20, 20, True)
plt.show()
