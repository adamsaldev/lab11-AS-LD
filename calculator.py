"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
<<<<<<< HEAD
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot calculate the square root of a negative number.")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except (TypeError, ValueError):
        raise ValueError("Invalid arguments for hypotenuse.")

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments.")
    return math.log(b, a)


def exp(a, b):
    return a ** b
=======
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def log(a, b):
    if a<= 0 or a==1 or b<=0:
        raise ValueError("Invalid logarithm")
    return math.log(b, a)

def exp(a, b):
    return a**b

>>>>>>> a89214d38d1705879e7dbb2553443e88401e3c9a


