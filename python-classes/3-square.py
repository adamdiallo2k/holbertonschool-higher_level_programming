#!/usr/bin/python3
"""A module for representing a square."""


class Square:
    """A class to represent a square with methods to calculate its area."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
