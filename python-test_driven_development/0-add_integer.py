#!/usr/bin/python3
"""
This module contains the implementation of a function named `add_integer` that adds two numbers together, either integers or floats.
"""

def add_integer(a, b=98):
    """
    This function adds two numbers together, either integers or floats. If either `a` or `b` is not a number, a `TypeError` is raised.

    Parameters:
    a (int or float): The first number to add.
    b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
    int: The sum of `a` and `b` after converting them to integers if they are of type float.

    Raises:
    TypeError: If either `a` or `b` is not of type int or float.
    """
    if b is None:
        raise TypeError("b must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return a + b

