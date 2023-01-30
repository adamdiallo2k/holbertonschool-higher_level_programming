#!/usr/bin/python3
"""
This module contains the definition of the Square class
"""


class Square:
    """
    A class representing a Square, with a size attribute.
    """
    __size = 0

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with default size 0

        Args:
        size (int): The size of the Square, with a default value of 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
        """
        self.__init__(value=size)

    def __init__(self, value):
        """
        Initializes a new instance of the Square class with size attribute

        Args:
        value (int): The size of the Square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is negative.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Returns the area of the Square.
        """
        return self.__size * self.__size
