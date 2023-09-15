#!/usr/bin/python3
"""
This module contains the function definition of
print_square
"""


def print_square(size):
    """
    Print as square using '#' symbol of size 'size'
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for length in range(0, size):
        for height in range(0, size):
            print("#", end="")
        print()
