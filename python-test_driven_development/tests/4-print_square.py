#!/usr/bin/python3
""" module """
def print_square(size):
    """
    This function prints a square of a given size using the `#` character.

    Args:
    size (int): The size of the square, must be a non-negative integer.

    Raises:
    TypeError: If `size` is not of type `int`.
    ValueError: If `size` is negative.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

