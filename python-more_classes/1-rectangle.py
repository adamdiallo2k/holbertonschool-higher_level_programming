#!/usr/bin/python3
"""
This module contains the class Rectangle, which represents a rectangle.
"""

# Define a class to represent a rectangle
class Rectangle:
    """
    Define a rectangle by its width and height.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Raises:
        TypeError: If the value passed as `width` or `height` is not an integer.
        ValueError: If the value passed as `width` or `height` is less than 0.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
