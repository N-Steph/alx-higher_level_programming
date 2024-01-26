#!/usr/bin/python3

"""
Script that fetches 'https://alx-intranet.hbtn.io/status'
"""

from urllib.request import urlopen


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        response_body = response.read()
        print("Body response:")
        print("    - type: {}".format(type(response_body)))
        print("    - content: {}".format(response_body))
        print("    - utf8 content: {}".format(response_body.decode('utf-8')))
