#!/usr/bin/python
"""Definition of function that checks if an objects class is is a subclass\
 of another one
"""


def inherits_from(obj, a_class):
    """Returns True of 'obj' class is a subclass of 'a_class'.
    Otherwise return False
    """
    if type(obj) is a_class:
        return False
    return issubclass(obj.__class__, a_class)
