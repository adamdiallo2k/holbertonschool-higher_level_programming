#!/usr/bin/python3
""" module """
class MyList(list):
    def print_sorted(self):
        """
        This function takes a list as an argument, sorts a copy of the list in ascending order using a for loop, and then prints the sorted list. The original list is not modified.

        Args:
        lst (list): The list to be sorted and printed.

        Returns:
        None
        """
        sorted_list = self[:]
        for i in range(len(sorted_list)):
            for j in range(i + 1, len(sorted_list)):
                if sorted_list[i] > sorted_list[j]:
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
        print(sorted_list)

