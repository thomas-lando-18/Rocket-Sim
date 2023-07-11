import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy.integrate import trapezoid, simpson


# Functions

"""
Trapezoidal Integration
"""
def integrate_trap(x: list, y: list):
    ans = trapezoid(y, x, dx=(x[1]-x[0]))
    return ans

"""
Simpsons Integration
"""
def integrate_simp(x: list, y: list):
    ans = simpson(y, x, dx=(x[1]-x[0]))
    return ans
