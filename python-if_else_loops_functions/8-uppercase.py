#!/usr/bin/python3

def uppercase(str):
    result = ''
    for char in str:
        if 97 <= ord(char) <= 122:  # ASCII values for 'a' to 'z'
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char
    print("{}".format(result))
