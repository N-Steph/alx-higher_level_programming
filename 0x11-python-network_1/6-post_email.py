#!/usr/bin/python3

"""
This script sends a POST request email as parameter and displays the body
of the response
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    response = requests.get(url, param={'email', argv[2]})
    print(response.text)
