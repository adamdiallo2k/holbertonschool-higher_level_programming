#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list3 = []
    
    for i in range(list_length):
        try:
            my_list3.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            my_list3.append(0)
        except ZeroDivisionError:
            print("division by 0")
            my_list3.append(0)
        except TypeError:
            print("wrong type")
            my_list3.append(0)
        finally:
            if i == list_length - 1:
                return my_list3
