#!/usr/bin/python3
"""
1. My list
A class MyList that inherits from list
"""


class MyList(list):
    """Class MyList that inherits from list
    Args:
        list
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        """
        print(sorted(self))
