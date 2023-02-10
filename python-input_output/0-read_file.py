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
    with open(filename, "r") as file:
        """
        Open the file using a with statement to ensure that the file is properly closed after reading.
        """
        content = file.read()
        """
        Read the entire content of the file into a variable called content.
        """
    print(content)
    """
    Print the content of the file.
    """
