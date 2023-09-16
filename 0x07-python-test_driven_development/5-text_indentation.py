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
    i = 0
    while i < len(text):
        while text[i] == " " or text[i] == "    ":
            i += 1
        print("{}".format(text[i]), end="")
        if text[i] in punctuation:
            print()
            print()
            if text[i + 1] == " " or text[i] == "   ":
                i += 2
                continue
        i += 1
