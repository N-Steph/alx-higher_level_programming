#!/usr/bin/python3
"""This script adds all arguments to a Python list and then
save them to a file
"""


import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    des_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    with open('add_item.json', mode='w', encoding='utf-8') as file_open:
        _list = []
        for i in range(1, len(sys.argv)):
            _list.append(sys.argv[i])
        json.dump(_list, file_open)
    sys.exit()
for i in range(1, len(sys.argv)):
    des_list.append(sys.argv[i])
save_to_json_file(des_list, 'add_item.json')
