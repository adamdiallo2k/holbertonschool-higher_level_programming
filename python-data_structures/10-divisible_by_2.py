#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length_list = [None] * len(my_list)
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            length_list[i] = True
        else:
            length_list[i] = False
    return length_list

