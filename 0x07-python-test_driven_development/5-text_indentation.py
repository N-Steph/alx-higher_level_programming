#!/usr/bin/python3
"""
This module contains the defintion of text_indentation
function
"""


def text_indentation(text):
    """
    Print the text in 'text' with 2 new lines after each
    of the character: ., ? and :
    """
    punctuation = ['.', '?', ':']

    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        print("{}".format(char), end="")
        if char in punctuation:
            print()
            print()
