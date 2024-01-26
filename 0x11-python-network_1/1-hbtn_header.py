#!/usr/bin/python3

"""
This script display the value of X-Request-Id found in the header of the
response from the request sent
"""

from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        header_info = response.info()
        print(header_info['X-Request-id'])
