#!/usr/bin/python3
"""A module that contains the Square class."""
from models.rectangle import Rectangle
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
    def __str__(self):
        """
        Return a string representation of the Square object.

        Returns:
            A string in the format:
            [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Returns:
            None.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.height = kwargs['size']
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
