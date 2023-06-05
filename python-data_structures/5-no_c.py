#!/usr/bin/env python3
def no_c(my_string):
    my_string2 = ""
    for i in range(len(my_string)):
       if not (my_string[i] == 'c' or my_string[i] == 'C'):
            my_string2 += my_string[i]
    return my_string2
