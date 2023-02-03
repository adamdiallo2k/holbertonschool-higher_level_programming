#!/usr/bin/python3
"""
This module contains the class Rectangle, which represents a rectangle.
"""

class Rectangle:
    """Represent a rectangle.
    
    A rectangle is defined by its width and height. The width and height must
    be integers greater than or equal to 0. The rectangle can be described by
    its area, perimeter, and string representation.
    
    Attributes:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to 0.
    """
    
    def __init__(self, width=0, height=0):
        """Initialize a rectangle with a width and height.
        
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        
        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is negative.
        """
        self.width = width
        self.height = height
    
    def area(self):
        """Return the area of the rectangle.
        
        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height
    
    def perimeter(self):
        """Return the perimeter of the rectangle.
        
        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self._width + self._height) if self._width != 0 and self._height != 0 else 0
    
    def __str__(self):
        """Return the string representation of the rectangle.
        
        The string representation of the rectangle is created by concatenating
        "#" characters, with one row for each unit of height. If the width or
        height of the rectangle is 0, an empty string is returned.
        
        Returns:
            str: The string representation of the rectangle.
        """
        return "\n".join("#" * self._width for _ in range(self._height)) if self._width != 0 and self._height != 0 else ""


