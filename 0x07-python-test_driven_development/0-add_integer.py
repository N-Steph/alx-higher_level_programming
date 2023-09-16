#!/usr/bin/python3
"""This module defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """Adds two integers and returns the result"""
    num_type = [int, float]
    arguments = [a, b]
    arguments = {"a": a, "b": b}
    for key, value in arguments.items():
        if value is None or type(value) not in num_type:
            raise TypeError("{} must be an integer".format(key))
    if type(a) is num_type[1] or type(b) is num_type[1]:
        a = int(a)
        b = int(b)
    return a + b
