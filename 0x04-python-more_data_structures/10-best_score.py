#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value
    """
    if len(a_dictionary) == 0 or a_dictionary == None:
        return None
    biggest = a_dictionary[list(a_dictionary)[0]]
    biggest_key = list(a_dictionary)[0]
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = a_dictionary[key]
            biggest_key = key
    return biggest_key
