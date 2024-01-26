#!/usr/bin/python3

"""
This script displays the body of a response and handle erros and exceptions
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    response = requests.get(url)
    code = response.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)
