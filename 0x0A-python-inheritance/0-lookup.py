#!/usr/bin/python3
"""lookup function definition.
Returns the all attributes and methods of the object passed to it.
"""


def lookup(obj):
    """Returns a list of all attributes and methods of 'obj'"""
    return dir(obj)
