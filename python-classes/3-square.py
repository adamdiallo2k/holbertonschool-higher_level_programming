#!/usr/bin/python3

"""
This module contains the definition of the Square class.
The Square class represents a square with a size.
"""


class Square:
     """
    Represents a square with a size.
    """
    __size = 0

    def __init__(self, size=0):
        """
        Initialize a new instance of the Square class.

        :param size: The size of the square. Must be an integer >= 0.
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size


    def area(self):
        """
        Calculates the area of the square.

        :return: The area of the square.
        """
        return self.__size * self.__size

