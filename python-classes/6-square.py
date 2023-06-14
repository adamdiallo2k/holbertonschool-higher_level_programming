#!/usr/bin/python3
"""A module for representing a square."""


class Square:
    """A class to represent a square with methods to calculate its area."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """gets the size of the square"""
        return self.__position

    @size.position
    def position(self, value):
        """set the position"""
        for i in range(len(value)):
            if value[i] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position[i] = value[i]

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
        else:
             print("\n" * self.position[1], end="")
             print("\n".join(" " * self.position[0] + "#" * self.__size for _ in range(self.__size)))
