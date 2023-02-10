#!/usr/bin/python3
"""
Module for loading objects from JSON files.

This module provides a function `load_from_json_file` that takes a filename as input and returns the object represented by the contents of the JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Function to load an object from a JSON file.

    Parameters:
    filename (str): The name of the JSON file.

    Returns:
    object: The object represented by the contents of the JSON file.
    
    Example:
    >>> load_from_json_file("example.json")
    {'key1': 'value1', 'key2': 'value2'}
    """
    with open(filename, 'r') as f:
        return json.load(f)
