#!/usr/bin/python3
"""Definition of add_attribute function"""


def add_attribute(obj, attr, value):
    """Adds an attribute 'attr' to object 'object' with value 'value'.
    raise TypeError exception if we can't add attribute 'attr'
    """
    object_type = [int, float, str, bool, list, set, tuple, None]
    if type(obj) in object_type:
        raise TypeError("can't add new attribute")
    if 'slots' in dir(obj):
        if attr not in obj.slots:
            raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
