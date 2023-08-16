#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary
    """
    del a_dictionary[key]
    return a_dictionary
