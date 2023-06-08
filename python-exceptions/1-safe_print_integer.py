#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        if (isinstance(value, int) == False):
            return False
    return True
