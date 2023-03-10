#!/usr/bin/python3
""" Module """


class BaseGeometry:
    """ class doc """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ doc """
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
