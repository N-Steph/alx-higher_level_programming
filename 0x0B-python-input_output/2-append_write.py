#!/usr/bin/python3
"""Defines a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string to a text file and
    returns the number of characters written
    """
    data_type = [int, bool, float]
    data_obj = [filename, text]

    if filename is None or filename == "" or text is None:
        return
    for data in data_obj:
        if data == data_obj[0] and type(data) in data_type:
            filename = str(data)
        elif data == data_obj[1] and type(data) in data_type:
            text = str(data)
    with open(filename, mode='a', encoding='utf-8') as file_open:
        return file_open.write(text)
