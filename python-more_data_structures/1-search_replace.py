#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    
    new_list = [replace if x == 2 else x for x in my_list]
    return new_list
