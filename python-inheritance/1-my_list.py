#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        """
        This function takes a list as an argument, sorts the list in ascending order using a for loop, and then prints the sorted list.

        Args:
        lst (list): The list to be sorted and printed.

        Returns:
        None
        """
        for i in range(len(self)):
            for j in range(i + 1, len(self)):
                if self[i] > self[j]:
                    self[i], self[j] = self[j], self[i]
        print(self)
