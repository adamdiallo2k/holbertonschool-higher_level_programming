#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = [0 for i in range(list_length)]
    for i in range(list_length):
        try:
            my_list_3[i] += my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            # code to run regardless of whether an exception was raised
            pass
    return my_list_3
