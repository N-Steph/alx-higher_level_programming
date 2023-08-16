#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Sum unique integers in a list
    Return the sum
    """
    unique_elements = list(set(my_list))
    add = 0
    for integer in unique_elements:
        add = add + integer
    return add
