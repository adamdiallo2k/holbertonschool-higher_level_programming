#!/usr/bin/python3

for ch in range(97, 123):
    if (chr(ch) != "q" and chr(ch) != "e"):
        print("{:c}".format(ch), end='')
