#!/usr/bin/python3
def max_integer(my_list=[]):
    
    if (len(my_list) > 0):
        maxi = -32456789
        for i in range(len(my_list)):
            if (maxi < my_list[i]):
                maxi = my_list[i]
        return maxi
