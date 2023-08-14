#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """This function prints all integers of a list in reverse order"""
    last_idx = -(len(my_list) + 1)
    for i in range(-1, last_idx, -1):
        print("{:d}".format(my_list[i]))
