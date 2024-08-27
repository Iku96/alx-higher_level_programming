#!/usr/bin/python3
"""
This module defines a custom list class that includes an additional method
for printing the list in sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in list class with an additional method
    to print the list in sorted order.
    """

    def __init__(self):
        """
        Initializes a new instance of MyList by calling the parent class
        initializer.
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method does not modify the original list but prints a sorted
        version of it.
        """
        sorted_list = sorted(self)
        print(sorted_list)
