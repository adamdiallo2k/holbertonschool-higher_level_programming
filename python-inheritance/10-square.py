#!/usr/bin/python3
""" Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Square(BaseGeometry):
    """ Write a class Square that inherits from Rectangle """
    def __init__(self, size):
        super().integer_validator("size", size)
        self._size = size
    
    def area(self):
        return self._size ** 2
    def __str__(self):
        return "[Rectangle] {}/{}".format(self._size, self._size)
