#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Read a text file and prints to stdout
    Args:
        filename (string): path + filename to read
    """
    with open(filenmae, mode='r', encoding='utf-8') as file_open:
        print(file_open.read())
