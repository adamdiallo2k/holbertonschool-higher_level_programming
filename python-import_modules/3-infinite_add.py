#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum_args = sum(int(arg) for arg in sys.argv[1:])
    print(sum_args)
