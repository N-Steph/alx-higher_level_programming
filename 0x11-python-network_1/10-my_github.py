#!/usr/bin/python3

"""
This script displays id of a GitHub user when passed username and password
as credentials
"""

from requests.auth import HTTPBasicAuth
from requests import get
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user, password = argv[1], argv[2]
    basic = HTTPBasicAuth(user, password)
    response = get(url, auth=basic)
    print(response.headers.get('id'))
