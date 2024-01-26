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
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode('utf-8')))
