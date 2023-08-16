#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element by another in a new list
    Return the new list
    """
    new_list = my_list.copy()
    for index, element in enumerate(my_list):
        if element == search:
            new_list[index] = replace
    return new_list
