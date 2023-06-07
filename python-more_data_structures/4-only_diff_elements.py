#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_3 = set()
    for x in set_1:
        if x not in set_2 and x not in set_3:
            set_3.add(x)
    for y in set_2:
        if y not in set_1 and y not in set_3:
            set_3.add(y)
    return set_3
