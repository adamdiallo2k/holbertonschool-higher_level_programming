#!/usr/bin/python3
"""
Module for saving Python objects to text files in JSON format.

This module provides a single function, `save_to_json_file`, which takes a Python object and a file name as input
and writes the JSON representation of the object to the file. The conversion from Python object to JSON string
is performed using the `json.dump` function from the `json` module, which is a built-in module in Python.

Functions:
    save_to_json_file(my_obj, filename)
        Writes a Python object to a text file in JSON format.
        
        Arguments:
            my_obj (object) -- the Python object to be written
            filename (str) -- the name of the file to write to
        
        Returns:
            None
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Arguments:
    my_obj -- the Python object to be written
    filename -- the name of the file to write to

    Returns:
    None
    """
    
    # Open the file in write mode and use the with statement to ensure it is properly closed
    with open(filename, 'w') as f:
        
        # Use the json.dump function to serialize the Python object into a JSON string and write it to the file
        json.dump(my_obj, f)
