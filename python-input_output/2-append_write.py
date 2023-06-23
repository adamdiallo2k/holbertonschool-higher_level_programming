#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """function"""
    with open(filename, 'a') as f:
        f.write(text)
    
    with open(filename, "r", encoding="utf-8") as g:
        contents = g.read()
    return len(contents)
