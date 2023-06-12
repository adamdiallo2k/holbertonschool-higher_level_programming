#!/usr/bin/python3

class Square:
    """module"""
    def __init__(self, size=0):
        if isinstance(size, int) == True:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size