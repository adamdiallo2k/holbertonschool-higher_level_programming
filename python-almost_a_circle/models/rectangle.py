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
        Prints in the standard output the Rectangle
        instance with the character '#' in a grid.
        The instance position in the grid is determined
        by the x and y attributes. It does not return anything.

        Args:
            None

        Returns:
            None
        """
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for z in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print("")
    def __str__(self):
        """
        Returns a string representation of the Rectangle
        object in the format: [Rectangle] (<id>) <x>/<y> <width>/<height>
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    def update(self, *args, **kwargs):
        """
    Update the Rectangle attributes using *args and **kwargs.

    Args:
        *args: Variable length argument list.
            args[0] (int, optional): The ID of the rectangle.
            args[1] (int, optional): The width of the rectangle.
            args[2] (int, optional): The height of the rectangle.
            args[3] (int, optional): The x-coordinate of the rectangle.
            args[4] (int, optional): The y-coordinate of the rectangle.
        **kwargs: A dictionary of keyword arguments that can be
            passed to update the Rectangle attributes.

    Returns:
        None.
    """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
