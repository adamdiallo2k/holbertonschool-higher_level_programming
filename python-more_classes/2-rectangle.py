#!/usr/bin/python3
"""
This module contains the class Rectangle, which represents a rectangle.
"""
class Rectangle:
    """
    Defines a Rectangle with private instance attributes `width` and `height`.
    """
    
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with optional `width` and `height`.
        """
        self.width = width
        self.height = height
    
    @property
    def height(self):
        """
        Getter for private instance attribute `height`.
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Setter for private instance attribute `height`.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Getter for private instance attribute `width`.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for private instance attribute `width`.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    def area(self):
        """
        Returns the rectangle's area.
        """
        return self.__width * self.__height
    
    def perimeter(self):
        """
        Returns the rectangle's perimeter.
        If width or height is equal to 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

