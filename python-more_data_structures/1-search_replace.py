#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mynewlist = []
    for i in range(len(my_list)):
        if (my_list[i] == search):
            mynewlist.append(replace)
        else:
            mynewlist.append(my_list[i])
    return mynewlist
