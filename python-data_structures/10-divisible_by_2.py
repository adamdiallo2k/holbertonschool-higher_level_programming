#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    listresult = [0] * len(my_list)

    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            listresult[i] = True
        else:
            listresult[i] = False
    return listresult
