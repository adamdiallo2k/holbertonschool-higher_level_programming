#!/usr/bin/python3
"""commented module"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update attributes based on arguments"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
            """Return a dictionary representation of the Square"""
            return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
