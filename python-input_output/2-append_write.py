#!/usr/bin/python3
"""
Module for writing a string to a text file.
"""

def append_write(filename="", text=""):
    """
    Append a string to a text file.

    Arguments:
    filename (str, optional): The name of the file to be written. Defaults to an empty string.
    text (str, optional): The string to be written to the file. Defaults to an empty string.

    Returns:
    int: The number of characters written to the file. Returns 0 if no `filename` is provided.
    """
    if (filename):
        with open(filename, "a", encoding="utf-8") as file:
            # Write the text to the file
            content = file.write(text)
        # Return the number of characters written to the file
        return len(text)
    else:
        return 0
