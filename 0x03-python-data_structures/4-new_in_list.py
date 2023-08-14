#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Creates a copy of my_list and
    Replaces element at index 'idx' with 'element'
    the copy of my_list.
    Returns copy of my_list
    """
    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
