#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two numbers together, either integers or floats.
    If either `a` or `b` is not a number, a TypeError is raised.

    Parameters:
    a (int or float): The first number to add.
    b (int or float, optional): The second number to add, default is 98.

    Returns:
    int: The sum of `a` and `b`.

    Raises:
    TypeError: If either `a` or `b` is not a number.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return a + b
