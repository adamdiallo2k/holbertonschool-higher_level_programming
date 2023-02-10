#!/usr/bin/python3
"""
Module for converting a Python object to a JSON-formatted string.
"""
import json
from io import StringIO

def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.
    
    Arguments:
    my_obj (object): The Python object to be converted to a JSON-formatted string.
    
    Returns:
    str: The JSON-formatted string representation of the Python object.
    """
    json_data = StringIO()
    json.dump(my_obj, json_data)
    return json_data.getvalue()
