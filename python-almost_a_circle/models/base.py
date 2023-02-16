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
    
    def to_json_string(list_dictionaries):
         """
        Returns a JSON string representation of a Square instance.
        """
        return json.dumps(list_dictionaries)
