#!/usr/bin/python3
"""commented module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
    def area(self):
        """return area of rectangle"""
        return self.__height * self.__width
    
    def __str__(self):
        """return return, the following rectangle 
        description: [Rectangle] <width>/<height> """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
