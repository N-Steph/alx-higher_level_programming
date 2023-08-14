#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Delete item at index 'idx' from 'my_list'
    Return the my_list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
