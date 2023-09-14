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
        json.dump([], file_open)
    sys.exit()
for i in range(1, len(sys.argv)):
    des_list.append(sys.arv[i])
save_to_json_file(des_list, 'add_item.json')
