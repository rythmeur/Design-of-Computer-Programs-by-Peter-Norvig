# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the
# non-negative numbers. The runtime of your program should be
# proportional to the LOGARITHM of the input. You may want to
# do some research into binary search and Newton's method to
# help you out.
#
# This function should return another function which computes the
# inverse of the input function.
#
# Your inverse function should also take an optional parameter,
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is
# efficient enough.

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""

    def derivative(f): # Newton's method
        """Computes the numerical derivative of a function."""
        def df(x, h=0.1e-3):
            der = ( f(x+h/2) - f(x-h/2) )/h
            return der if der!=0 else 0.00001
        return df

    def f_1(y):
        x = y/2.0
        while abs(f(x)- y) > delta :
            x = x - (f(x)-y)/derivative(f)(x)
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1

    # def f_1(y):
    #     x, x1 = -100, 100
    #     x2 = 1000
    #     fx1 = f(x1) - y
    #     fx2 = f(x2) - y
    #     while abs(x1-x2) > delta :
    #         x=x1 - 1.0* fx1 * (x1-x2) / fx1 - fx2
    #         x2=x1
    #         x1=x
    #         fx1 = f(x1) - y
    #         fx2 = f(x2) - y
    #         print x,x1,x2
    #     return x if (f(x)-y < y-f(x-delta)) else x-delta


    return f_1



def square(x): return x**2
sqrt = slow_inverse(square)

sqrt2 = inverse(square)

print sqrt(1000000000)
print sqrt2(1000000000)