#!/usr/bin/python3
"""
This script adds two numbers using a function imported from another module.
"""

if __name__ == "__main__":
    """
    This block is executed if the script is run directly, not imported as a module.
    """
    from add_0 import add

a = 1
b = 2

print("{} + {} = {}".format(a, b, add(a, b)))
