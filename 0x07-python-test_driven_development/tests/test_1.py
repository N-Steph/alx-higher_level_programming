#!/usr/bin/python3
"""This module defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """Adds two integers and returns the result"""
    num_type = [int, float]
    if type(a) not in num_type:
        raise TypeError("a must be an integer")
    else:
        if type(a) is num_type[1]:
            a = int(a)
    if type(b) not in num_type:
        raise TypeError("b must be an integer")
    else:
        if type(b) is num_type[1]:
            b = int(b)
    return a + b
