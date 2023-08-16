#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.
    """
    keys = sorted(a_dictionary)
    new_dict = {}
    for key in keys:
        new_dict[key] = a_dictionary[key]
    for key, value in new_dict.items():
        print("{}: {}".format(key, value))
