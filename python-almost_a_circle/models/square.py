#!/usr/bin/python3
from models.rectangle import Rectangle
"""A module that contains the Square class."""
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
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
