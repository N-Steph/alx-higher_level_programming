#!/usr/bin/python3
"""Defines a function that writes an object to a text file, using
a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Write to a text file and returns the number of characters written
    """
    data_type = [int, bool, float]

    if filename is None or filename == "":
        return
    if type(filename) in data_type:
        filename = str(filename)
    with open(filename, mode='w', encoding='utf-8') as file_open:
        json.dump(my_obj, file_open)
