#!/usr/bin/python3

"""
This script takes in a letter and sends a POST request to
'http://0.0.0.0:5000/search_user
"""

import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) < 2:
        letter = {'q': ""}
    else:
        letter = {'q': argv[1]}
    response = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
    if len(json_data) == 0:
        print("No result")
    else:
        print("[{}] {}".format(json_data['id'], json_dat['name']))
