#!/usr/bin/python3

"""
This script sends a post request to a url with an email as parameter.
The URL and email are passed as command line arguments to the script
"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}
    data = urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
