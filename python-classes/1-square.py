#!/usr/bin/python3

"""This module contains the Square class.

The Square class represents a square and has the following attributes:
- size
"""

class Square:
    """This class represents a square.
    
    It has the following attributes:
    - size
    """
    __size = 0

    def __init__(self,new_size):
        """Initialize a new Square with a given size."""
        self.__size = new_size
