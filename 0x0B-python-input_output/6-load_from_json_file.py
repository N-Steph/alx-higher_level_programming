#!/usr/bin/python3
"""This module contains definition of a function that creates an
Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    if type(filename) is not str:
        return
    with open(filename, mode='r', encoding='utf-8') as file_open:
        return json.load(file_open)
