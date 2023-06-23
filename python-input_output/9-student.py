#!/usr/bin/python3
"""module that adds all arguments to a Python list, and then saved to a file"""


class Student:
    """class docx"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function doc"""
        return self.__dict__
