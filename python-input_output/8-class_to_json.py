#!/usr/bin/python3
""" Module """
def class_to_json(obj):
    """
    Function to return a dictionary representation of an object for JSON serialization.

    Parameters:
    obj (object): The object to be serialized.

    Returns:
    dict: The dictionary representation of the object.
    """
    obj_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[key] = value
    return obj_dict
