#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element at a particular index from a list
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]