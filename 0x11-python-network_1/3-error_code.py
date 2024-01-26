#!/usr/bin/python3

"""
This script displays the body of an HTTP response, managine the HTTPError
exception
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    try:
        response = urlopen(url)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    else:
        with response:
            print(response.read().decode('utf-8'))
