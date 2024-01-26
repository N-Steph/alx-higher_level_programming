#!/usr/bin/python3

"""
This script takes in a letter and sends a POST request to
'http://0.0.0.0:5000/search_user
"""

import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) < 2:
        data = {'q': ""}
    else:
        data = {'q': argv[1]}
    response = requests.get('http://0.0.0.0:5000/search_user', param=data)
    try:
        json_data = response.json()
        print("[{}] {}".format(json_data['id'], json_data['name']))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
    else:
        print("No result")
