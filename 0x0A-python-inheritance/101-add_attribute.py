#!/usr/bin/python3
"""Definition of add_attribute function"""


def add_attribute(obj, attr, value):
    """Adds an attribute 'attr' to object 'object' with value 'value'.
    raise TypeError exception if we can't add attribute 'attr'
    """
    object_type = [int, float, str, bool, list, set, tuple, None]
    attr_exception = TypeError("can't add new attribute")
    if type(obj) in object_type:
        raise attr_exception
    if 'slots' in dir(obj):
        if attr not in obj.slots:
            raise attr_exception
    if '__slots__' in dir(obj):
        if attr not in obj.__slots__:
            raise attr_exception
    obj.__dict__[attr] = value
