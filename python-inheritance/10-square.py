#!/usr/bin/python3
""" 
Module that defines a class Square that inherits from class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle

# Class definition
class Square(Rectangle):
    """ 
    Class Square that inherits from Rectangle

    Attributes:
    __size (int): private size of the square
    """
    def __init__(self, size):
        """
        Initialization method for Square class
        
        Args:
        size (int): size of the square

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than or equal to 0
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Method to calculate the area of the square

        Returns:
        int: area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Method to return the string representation of the square

        Returns:
        str: string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

