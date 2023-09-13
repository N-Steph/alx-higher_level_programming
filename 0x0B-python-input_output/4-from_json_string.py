#!/usr/bin/python3
"""This module contain a function that returns an object
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """Returns an object presented by JSON string(my_str)"""
    return json.loads(my_str)
