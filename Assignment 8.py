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
from numpy.linalg import norm, inv, eig

# Task 1

class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def add(self, c):
        return f'{c.real + self.real} + {c.img + self.img}i'

    def sub(self, c):
        return f'{c.real + self.real} - {c.img + self.img}i'
    
    def mul(self, c):
        return f'{c.real * self.real - c.img * c.img} + {c.real * self.img + c.img * self.real}i'

    def div(self, c):
        return f'{(c.real * self.real + c.img * self.img)/(c.real**2 + c.img**2)} + {(self.img * c.real - self.real * c.img)/(c.real**2 + c.img**2)}i'

c = ComplexNumber(2, 1)
z = ComplexNumber(3, 4)
print(c.div(z))