#!/usr/bin/python3
""" commented module"""


def read_file(filename=""):
    """commented function"""
    with open(filename, "r") as f:
        print(f.read(), end="")
