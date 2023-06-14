#!/usr/bin/python3
"""A module for representing a square."""


class Square:
    """A class to represent a square with methods to calculate its area."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the Square."""
        valid = 0
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in range(len(value)):
                if not isinstance(value[i], int) or value[i] < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
                else:
                    valid += 1
            if valid == 2:
                self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.position[1], end="")
            print("\n".join(" " * self.position[0] + "#" * self.__size for _ in range(self.__size)))
