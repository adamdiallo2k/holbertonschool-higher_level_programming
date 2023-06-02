#!/usr/bin/python3
if __name__ == "__main__":
    import sys

num_args = len(sys.argv) - 1

if (num_args == 1):
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))

else:
    print("{} arguments".format(num_args))
    if (num_args > 0):
        i = 1
        for i in range(num_args):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
