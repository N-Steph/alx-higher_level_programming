#!/usr/bin/python3
def add_attribute(obj, attr, value):
    object_type = [int, float, str, bool, list, set, tuple, None]
    if type(obj) in object_type:
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
