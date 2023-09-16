#!/usr/bin/python3
"""
This module contains the definition of the function
say_my_name
"""


def say_my_name(first_name, last_name):
    """
    Prints the a string to the stdout containing the first_name
    and last_name argument passed to it.
    """
    data = {"first_name": first_name, "last_name": last_name}
    for key, value in data.items():
        if type(value) is not str:
            raise TypeError("{} must be a string".format(key))
    print("My name is {} {}".format(first_name, last_name))
