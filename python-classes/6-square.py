#!/usr/bin/python3
"""
This module contains the definition of the Square class.
"""


class Square:
    """
    A class representing a Square, with a size attribute.
    """
    def __init__(self, size=0, position=(0,0)):
        """
        Initializes a new instance of the Square class.

        Args:
        size (int): The size of the Square, with a default value of 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
        """
        self.position = position
        self.size = size
    @property
    def position(self):
        """
        Property getter for the position attribute of the Square.

        Returns:
        int: The position of the Square.
        """
        return self.__position
    

    @position.setter
    def position(self,value):
        """
        Property setter for the position attribute of the Square.

        Args:
        value (tuple): The new position of the Square.

        Raises:
        TypeError: If value is not a tuple..
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
        



    @property
    def size(self):
        """
        Property getter for the size attribute of the Square.

        Returns:
        int: The size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter for the size attribute of the Square.

        Args:
        value (int): The new size of the Square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Returns the area of the Square.
        """
        return self.__size * self.__size

    def my_print(self):
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")
