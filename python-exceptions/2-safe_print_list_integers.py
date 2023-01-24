#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for char in my_list:
            counter += 1
    for i in range(x):
        try:
            int(my_list[i])
            print("{:d}".format(list[i]))
        except IndexError as e:
            print(f"{e}")
        except ValueError:
            pass
