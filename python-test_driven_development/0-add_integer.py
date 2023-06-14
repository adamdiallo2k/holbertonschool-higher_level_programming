#!/usr/bin/python3
"""module commented"""


def add_integer(a, b=98):
    """commented function"""
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or a float')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer or a float')
    return int(a) + int(b)
