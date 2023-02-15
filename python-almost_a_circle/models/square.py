#!/usr/bin/python3
from models.rectangle import Rectangle
"""A module that contains the Square class."""
class Square(Rectangle):
    """
    A class for creating square
    objects with unique integer IDs.
    Inherits from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object with a unique ID
        and the specified size, x-coordinate, and y-coordinate.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the
            upper-left corner of the square. Default is 0.
            y (int, optional): The y-coordinate of the upper-left
            corner of the square. Default is 0.
            id (int, optional): The ID to assign to the square.
            If not provided, a new unique ID will be generated.

        Attributes:
            id (int): The ID assigned to the square.
            size (int): The size of the square.
            x (int): The x-coordinate of the upper-left
            corner of the square.
            y (int): The y-coordinate of the upper-left
            corner of the square.

        Returns:
            None.
        """
        super().__init__(size,size,x,y,id)
        self.__size = size
    def __str__(self):
        """
        Return a string representation of the Square object.

        Returns:
            A string in the format:
            [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Returns:
            None.
        """
        self.__size = value
        self.width = value
        self.height = value
