#!/usr/bin/python3
"""
Module for writing a string to a text file.
"""

def write_file(filename="", text=""):
    """
    Write a string to a text file.

    Arguments:
    filename (str, optional): The name of the file to be written. Defaults to an empty string.
    text (str, optional): The string to be written to the file. Defaults to an empty string.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        content = file.write(text)

    return len(text)
