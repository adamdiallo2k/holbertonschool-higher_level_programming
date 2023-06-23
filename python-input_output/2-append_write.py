#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """function"""
    with open(filename, 'a') as f:
        f.write(text)

    return len(text)
