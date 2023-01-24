#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for char in my_list:
            counter += 1

        if x > counter:
            x = counter

        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
        print("{}".format(''))
        return  x
    except IndexError as e:
        print(f"{e}")
