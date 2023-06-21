#!/usr/bin/python3
"""module commented"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size):
        """
        Initializer for the Square instance.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Method that returns the area of the Square.
        """
        return self.__size * self.__size
    
    def __str__(self):
        """return return, the following Square 
        description: [Square] <size>/<size> """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
