# Import Packages
import math
import numpy as np
import matplotlib.pyplot as plt
import os

###################################################################################################################
# IEMS 351, HW 1, Fall 2024
# Please replace __________________please_type_your_answer_here__________________ by your answer
# In this python script, there are 8 TODO's
###################################################################################################################

# Bisection Search
def bisection_search(func, left, right, tol=1e-3, max_it=100):
    """
    :param func:
        a function object,
        example: def f(x):
                    return x*x
        func = f
    :param left: float,
        left endpoint of the interval, [left, right]
        example: given an interval [2,3], then left = 2
    :param right: float,
        right end point of the interval
        example: given an interval [2,3], then right = 3
    :param tol: float,
        tolerance level for the termination
        by default, it is 1e-3
    :param max_it: int
        maximum number of iterations
        by default, it is 100
    :return:
        mid: float,
        estimated root of func
    """
    print("======================================================================================\n")
    print("Bisection Search\n")
    # Check Corner Cases
    # Case 1: function value is already close to 0 either at left or right
    if abs(func(left)) <= tol:
        print("Warning: An estimated root is found before the bisection method. "
              "Please consider reducing the tolerance.\n")
        return left
    if abs(func(right)) <= tol:
        print("Warning: An estimated root is found before the bisection method. "
              "Please consider reducing the tolerance.\n")
        return right

    # Case 2: left endpoint is larger than or equal to right endpoint
    assert left < right, "An error is encountered in the bisection method: initial interval is not legit, " \
                         "left must be smaller than right!\n"

    # Case 3: function values at both endpoints of the interval do not have the oppositive signs
    assert func(left) * func(right) < 0, "A error is encountered in the bisection method: " \
                                         "func(left) func(right) must have oppositive signs!\n"

    # main loop
    # ======================================================================================
    # TODO: (1) compute the midpoint of the interval
    mid = (left+right)/2
    # ======================================================================================
    it_counter = 0

    print("Iteration {}, interval: [{},{}]\n".format(it_counter, left, right))
    while abs(func(mid)) > tol:
        # ===========================================
        # TODO: (2) compute the function value at the left endpoint of the interval
        func_val_left = func(left)
        # TODO: (3) compute the function value at the midpoint of the interval
        func_val_mid = func(mid)
        # ======================================================================================

        # ======================================================================================
        # TODO: (4) compare the signs and update the interval accordingly
        if func_val_left*func_val_mid>0:
            left = mid
        else:
            right = mid
        # ======================================================================================

        it_counter += 1
        # ======================================================================================
        # TODO: (5) compute the midpoint of the new interval
        mid = (left+right)/2
        # ======================================================================================
        # display the new interval
        print("Iteration {}, interval: [{},{}]\n".format(it_counter, left, right))
        if it_counter >= max_it:
            print("Warning: Maximum number of iterations is reached!\n")
            print("Output the last midpoint as the estimated solution.\n")
            return mid


    print("The root is found after {} iterations! \nEstimated root: {}, "
          "Function value at the estimated root: {}\n".format(it_counter, mid, func(mid)))
    return mid


# Newton's Method
def newton_root_search(func, init_guess, tol=1e-3, max_it=100):
    """
    :param func:
        a function object, which provides the both function value and gradient
        example: def f(x):
                    val = x * x
                    grad = 2 * x
                    return val, grad
        func = f
    :param init_guess: float,
        initial guess of the root
        example: -1
    :param tol:
        tolerance level for the termination
        by default, it is 1e-3
    :param max_it:
        maximum number of iterations
        by default, it is 100
    :return:
        est_root: float,
        estimated root of func
    """
    print("======================================================================================\n")
    print("Newton's Method\n")
    # set the iteration counter
    it_counter = 0
    # set the current estimated root
    est_root =  init_guess
    # ======================================================================================
    # TODO: (6) compute the function value and gradient
    value, gradient = func(init_guess)
    # ======================================================================================
    print("Iteration {}, x = {}, f(x) = {}, f'(x) = {}\n".format(it_counter, est_root, value, gradient))
    while abs(value) > tol:
        # ======================================================================================
        # TODO: (7) update the estimasted root
        est_root = est_root-value/gradient
        # ======================================================================================
        # increment the iteration counter
        it_counter += 1
        # ======================================================================================
        # TODO: (8) compute the function value and gradient the new estimated root
        value, gradient = func(est_root)
        # ======================================================================================
        # display the results
        print("Iteration {}, x = {}, f(x) = {}, f'(x) = {}\n".format(it_counter, est_root, value, gradient))
        if it_counter >= max_it:
            print("Warning: Maximum number of iterations is reached!\n")
            print("Output the last midpoint as the estimated solution.\n")
            return est_root

    print("The root is found after {} iterations! \nEstimated root: {}, "
          "Function value at the estimated root: {}\n".format(it_counter, est_root, value))
    return est_root




