#!/usr/bin/python3
""" Module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Square(BaseGeometry):


    """ Write a class Square that inherits from Rectangle """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
