# Import Packages
import math
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

from iems351_tools_hw1 import bisection_search, newton_root_search


# f(x) = x + cos(x) + exp(x)
def func1(x):
    return x + math.cos(x) + math.exp(x)


# f(x) = x^2
def func2(x):
    return x * x

# f(x) = x^3 * exp(3x) + x
def func3(x):
    return (x ** 3) * math.exp(3 * x) + x

# f(x) = x^2 - 3 x + 2
def func4(x):
    return x * x - 3 * x + 2

# f(x) = x + cos(x) + exp(x)
def func1_with_gradient(x):
    val = x + math.cos(x) + math.exp(x)
    grad = 1 - math.sin(x) + math.exp(x)
    return val, grad

# f(x) = x^2
def func2_with_gradient(x):
    val = x * x
    grad = 2 * x
    return val, grad

# f(x) = x^3 * exp(3x) + x
def func3_with_gradient(x):
    val = (x ** 3) * math.exp(3 * x) + x
    grad = 3 * (x ** 2) * math.exp(3 * x) + 3 * (x ** 3) * math.exp(3 * x) + 1
    return val, grad

# f(x) = x^2 - 3 x + 2
def func4_with_gradient(x):
    val = x * x - 3 * x + 2
    grad = 2 * x - 3
    return val, grad


if __name__ == '__main__':
    # output the results to a text file
    stdoutOrigin = sys.stdout
    sys.stdout = open("iems351_hw1_log.txt", "w")

    # Bisection method
    # function 1: f(x) = x + cos(x) + exp(x)
    print("######################################################################################\n")
    print("Using bisection method to find the root of f(x) = x + cos(x) + exp(x)\n")
    root_guess_b1 = bisection_search(func=func1, left=-3, right=3)

    # function 3:
    # f(x) = x^3 * exp(3x) + x
    print("######################################################################################\n")
    print("Using bisection method to find the root of f(x) = x^3 * exp(3x) + x\n")
    root_guess_b3 = bisection_search(func=func3, left=-1, right=1)

    # function 4: f(x) = x^2 - 3 x + 2
    print("######################################################################################\n")
    print("Using bisection method to find the root of f(x) = x^2 - 3 x + 2\n")
    root_guess_b4 = bisection_search(func=func4, left=0, right=1.5)

    # Newton's method
    # function 1: f(x) = x + cos(x) + exp(x)
    print("######################################################################################\n")
    print("Using Newton's method to find the root of f(x) = x + cos(x) + exp(x)\n")
    root_guess_n1 = newton_root_search(func=func1_with_gradient, init_guess=3)

    # function 2: f(x) = x^2
    print("######################################################################################\n")
    print("Using Newton's method to find the root of f(x) = x^2\n")
    root_guess_n2 = newton_root_search(func=func2_with_gradient, init_guess=-1)

    # function 3: x^3 * exp(3x) + x
    print("######################################################################################\n")
    print("Using Newton's method to find the root of f(x) = x^3 * exp(3x) + x\n")
    root_guess_n3 = newton_root_search(func=func3_with_gradient, init_guess=0.5)

    # function 4: f(x) = x^2 - 3 x + 2
    print("######################################################################################\n")
    print("Using Newton's method to find the root of f(x) = x^2 - 3 x + 2\n")
    root_guess_n4 = newton_root_search(func=func4_with_gradient, init_guess=0.5)

