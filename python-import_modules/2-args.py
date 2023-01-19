#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv
    if (argc - 1 == 0):
        print("{} arguments.".format(argc - 1))
    elif (argc - 1 == 1):
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))
