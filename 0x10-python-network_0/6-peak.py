#!/usr/bin/python3

"""
This script contains the defintion of find_peak function
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return
    peak_element = list_of_integers[0]
    i = 0
    for elm in list_of_integers:
        if i == 0:
            i += 1
            continue
        if list_of_integers[i - 1] < elm and list_of_integers[i + 1 ] < elm:
            peak_element = elm
            break
        i += 1
    return peak_element
