#!/usr/bin/python3

"""
This module defines a Rectangle
class, which inherits from the Base class,
for creating rectangle objects with unique integer IDs.
"""

from models.base import Base

class Rectangle(Base):

    """
    A class for creating rectangle
    objects with unique integer IDs.
    Inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
    
        """
        Initialize a Rectangle object with a unique
        ID and the specified width, height,
        x-coordinate, and y-coordinate.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the
            upper-left corner of the rectangle. Default is 0.
            y (int, optional): The y-coordinate of the upper-left
            corner of the rectangle. Default is 0.
            id (int, optional): The ID to assign to the rectangle.
            If not provided, a new unique ID will be generated.

        Attributes:
            id (int): The ID assigned to the rectangle.
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the upper-left
            corner of the rectangle.
            y (int): The y-coordinate of the upper-left
            corner of the rectangle.

        Returns:
            None.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
    Calculates and returns the area of the Rectangle object.

    Returns:
        The area of the Rectangle object.
    """
        return self.__height * self.__width
    
    def display(self):
        """
        Displays the rectangle on the console using the '#' character.

        Returns:
            None.
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print(f"#",end='')
            print("")
