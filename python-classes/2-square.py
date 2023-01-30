#!/usr/bin/python3

"""
This module contains the class Square which creates a square object.
"""


class Square:
    """
    The Square class creates a square object with a size attribute.

    Attributes:
        __size (int): The size of the square.
    """
    __size = 0

    def __init__(self, size=0):
        """
        The constructor for Square class.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
