#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Read a text file and prints to stdout
    Args:
        filename (string): path + filename to read
    """
    if filename is None or filename == "" or type(filename) is not str:
        return
    try:
        with open(filename, mode='r', encoding='utf-8') as file_open:
            print(file_open.read(), end="")
    except FileNotFoundError as e:
        print(e.args[1])
