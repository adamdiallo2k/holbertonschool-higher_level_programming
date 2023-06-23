#!/usr/bin/python3
"""commented module"""


def write_file(filename="", text=""):
    """commented function"""
    count = 0
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, "r", encoding="utf-8") as g:
        contents = g.read()
    return len(contents)
