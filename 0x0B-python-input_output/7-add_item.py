#!/usr/bin/python3
"""This script adds all arguments to a Python list and then\
save them to a file\
"""


import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename, my_list):
    """Add items to a file"""
    try:
        des_list = load_from_json_file(filename)
    except FileNotFoundError:
        with open(filename, mode='w', encoding='utf-8') as file_open:
            _list = []
            for i in range(1, len(my_list)):
                _list.append(my_list[i])
            json.dump(_list, file_open)
        sys.exit()
    for i in range(1, len(my_list)):
        des_list.append(my_list[i])
    save_to_json_file(des_list, 'add_item.json')


if __name__ == "__main__":
    add_item('add_item.json', sys.argv)
