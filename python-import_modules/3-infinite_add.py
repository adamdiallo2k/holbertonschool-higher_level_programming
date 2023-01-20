#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    sumnumber = 0
    for i in range(1, len(argv)):
        sumnumber += int(argv[i])
    print("{}".format(sumnumber))
