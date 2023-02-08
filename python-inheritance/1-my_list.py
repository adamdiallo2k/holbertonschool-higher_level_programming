#!/usr/bin/python3
""" Module """
class MyList(list):
    """
    A custom list class that inherits from the built-in list class and implements a print_sorted method.
    """
    def print_sorted(self):
        """
        This method sorts the list in ascending order and prints the sorted list.

        Returns:
            None
        """
        for i in range(len(self)):
            for j in range(i + 1, len(self)):
                if self[i] > self[j]:
                    self[i], self[j] = self[j], self[i]
        print(self)
