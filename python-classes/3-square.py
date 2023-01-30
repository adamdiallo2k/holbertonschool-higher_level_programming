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
        Initializes a new instance of the Square class
        
        Args:
        size (int): The size of the Square, with a default value of 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Returns the area of the Square.
        """
        return self.__size * self.__size

