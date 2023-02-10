#!/usr/bin/python3
"""
Module for converting JSON strings into Python objects.

This module provides a single function, `from_json_string`, which takes a JSON string as input and returns a
Python object representation of that string. The conversion is performed using the `json.loads` function
from the `json` module, which is a built-in module in Python.

Functions:
    from_json_string(my_str)
        Converts a JSON string into a Python object.
        
        Arguments:
            my_str (str) -- the JSON string to be converted
        
        Returns:
            A Python object representation of the JSON string.
"""

import json

def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.

    Arguments:
    my_str -- the JSON string to be converted

    Returns:
    A Python object representation of the JSON string.
    """
    
    # Use the json.loads function to parse the JSON string and convert it into a Python object
    python_obj = json.loads(my_str)
    
    # Return the resulting Python object
    return python_obj
