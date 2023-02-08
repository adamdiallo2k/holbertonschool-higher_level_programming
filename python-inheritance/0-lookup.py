#!/usr/bin/python3
""" Module """
def lookup(obj):
    """
    This function returns a list of all the attributes and methods available for a given object.

    Args:
        obj (object): The object for which the attributes and methods are to be listed.

    Returns:
        list: A list of strings, representing the attributes and methods of the given object.
    """
    return dir(obj)
