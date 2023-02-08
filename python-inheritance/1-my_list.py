#!/usr/bin/python3
""" Module """
class MyList(list):
    def print_sorted(self):
        """
        Prints a sorted copy of the list in ascending order. The original list remains unchanged.

        Returns:
        None
        """
        sorted_list = self[:]
        """
        Create a copy of the original list to sort, so the original list remains unchanged.
        """
        for i in range(len(sorted_list)):
            for j in range(i + 1, len(sorted_list)):
                if sorted_list[i] > sorted_list[j]:
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
        """
        Sort the copied list using a nested for loop and swap elements if the current element is greater than the next element.
        """
        print(sorted_list)
        """
        Print the sorted list.
        """
