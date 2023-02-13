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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Returns:
            None.
        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Returns:
            None.
        """
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the upper-left
        corner of the rectangle.

        Returns:
            The x-coordinate of the upper-left
            corner of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the upper-left
        corner of the rectangle.

        Args:
            value (int): The new x-coordinate of the
            upper-left corner of the rectangle.

        Returns:
            None.
        """
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the
        upper-left corner of the rectangle.

        Returns:
            The y-coordinate of the upper-left
            corner of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the upper-left
        corner of the rectangle.

        Args:
            value (int): The new y-coordinate of
            the upper-left corner of the rectangle.

        Returns:
            None.
        """
        self.__y = value
