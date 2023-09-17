#!/usr/bin/python3
"""Function that check if an object belongs to a class or a parent of that\
class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if 'obj' is an instance of 'a_class' of a parent class\
     of 'a_class'
    """
    return isinstance(obj, a_class)
