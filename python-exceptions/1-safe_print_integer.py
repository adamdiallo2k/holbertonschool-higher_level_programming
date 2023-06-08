#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        if not isinstance(value, int):
            return False
    return True
