#!/usr/bin/python3
"""Defining MyList class that inherites from the list class"""


class MyList(list):
    """MyList class inheriting from list class"""

    def print_sorted(self):
        """Creates a new list with elements sorted.
        Prints the new list to stdout
        """
        print(sorted(self))
