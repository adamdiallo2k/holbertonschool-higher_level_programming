#!/usr/bin/python3
"""commented module"""


class BaseGeometry:
    """A base class with a method for validating integer values."""

    @staticmethod
    def integer_validator(name, value):
        """
        A static method that checks if a value is a positive integer.

        Args:
            name (str): The name of the variable to check.
            value (int): The value of the variable to check.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than zero.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class that represents a rectangle and inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Both width and height must be positive integers.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
