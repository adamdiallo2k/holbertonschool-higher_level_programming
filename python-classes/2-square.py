#!/usr/bin/python3

class Square:
    """
    Square is a class that defines a square.

    A square is a shape with four equal sides and four right angles.
    """
    __size = 0


    def __init__(self, size=0):
        """
        This method is the constructor of the Square class.

        :param size: The size of the square
        :raises: TypeError if size is not an integer
                 ValueError if size is less than 0
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
