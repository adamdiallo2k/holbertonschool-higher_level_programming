#!/usr/bin/python3
def uniq_add(my_list=[]):
    anotherlist = []
    sum = 0
    for i in range(len(my_list)):
        unique = True
        for y in range(len(anotherlist)):
            if (my_list[i] == anotherlist[y]):
                unique = False
                break
        if unique:
            anotherlist.append(my_list[i])
    for z in range(len(anotherlist)):
        sum += anotherlist[z]
    return sum
