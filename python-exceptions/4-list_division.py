#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = [0 for i in range(list_length)]
    for i in range(list_length):
        try:
            if (not isinstance(my_list_1[i], (int, float))) or (not isinstance(my_list_2[i], (int, float))):
                raise ValueError("wrong type")
            else:
                my_list_3[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by zero")
            pass
        except IndexError:
            print("out of range")
            pass
        except ValueError:
            print("wrong type")
            pass

    return my_list_3
