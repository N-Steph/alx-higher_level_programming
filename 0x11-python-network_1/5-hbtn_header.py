#!/usr/bin/python3

"""
This script displays the value of X-Requet-Id in the response header
of a request sent using the requests library
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    response = requests.get(url)
    print(response.get('X-Request-Id'))
