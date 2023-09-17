#!/usr/bin/python3
"""Definition of function that test if an object belongs to a particular\
 class
"""


def is_same_class(obj, a_class):
    """Returns True if 'obj' is an instance of 'a_class'.
    Otherwise False
    """
    return isinstance(obj, a_class)
