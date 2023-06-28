#!/usr/bin/python3
"""commented module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
