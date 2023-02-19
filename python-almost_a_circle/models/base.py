#!/usr/bin/python3
"""
This module defines a Base class for creating objects with unique integer IDs.
"""
import json

class Base:
    """
    A class for creating objects with unique integer IDs.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object with a unique ID.

        Args:
            id (int, optional): The ID to assign to the object.
            If not provided, a new unique ID will be generated.

        Attributes:
            id (int): The ID assigned to the object.

        Returns:
            None.
        """
        if (id is not None):
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of a Square instance.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            cls (class): the class to which the objects belong.
            list_objs (list): the list of objects to be saved.

        Returns:
            None.

        Raises:
            None.

        Example:
            ExampleClass.save_to_file(list_of_objects)

        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            list_dicts = []
            for obj in list_objs:
                list_dicts.append(cls.to_dictionary(obj))
            file.write(cls.to_json_string(list_dicts))
