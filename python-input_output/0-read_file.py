#!/usr/bin/python3
""" Module """
def read_file(filename=""):
    """
    This function takes a filename as an argument and prints the content of the file.
    If no filename is provided, it will print an empty string.

    Arguments:
    filename (str): The name of the file to be read.

    Returns:
    None
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print(content)
