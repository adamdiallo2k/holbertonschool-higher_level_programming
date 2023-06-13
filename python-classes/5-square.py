#!/usr/bin/python3
"""A module for representing a square."""


class Square:
    """A class to represent a square with methods to calculate its area."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
