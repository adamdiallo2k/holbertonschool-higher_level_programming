#!/usr/bin/python3
"""Module"""
class Rectangle:
    """Class that defines a rectangle with width, height and print_symbol"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize width and height of rectangle.
        Increment the number of instances.

        Args:
        width: width of the rectangle, defaults to 0
        height: height of the rectangle, defaults to 0
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Return the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of rectangle

        Raises:
        TypeError: if width is not an integer
        ValueError: if width is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of rectangle

        Raises:
        TypeError: if height is not an integer
        ValueError: if height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of rectangle using print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            rectangle.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Return a string representation of rectangle to recreate instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Decrement the number of instances and print a message on deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

