#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds whether or not elements in a list are multiple of 2
    Returns a new list with boolean values
    True if the element at that position is a multiple of 2
    False otherwise
    """
    boolean_list = []
    for i in my_list:
        if i % 2 == 0:
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    return boolean_list
