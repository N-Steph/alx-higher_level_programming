#!/usr/bin/python3

"""
This script contains the defintion of find_peak function
"""


def find_peak(your_list):
    """Finds a peak in a list of unsorted integers"""
    len_list = len(your_list)
    if len_list == 0:
        return
    for i in range(1, len_list, 2):
        if your_list[i - 1] < your_list[i] and your_list[i + 1] < your_list[i]:
            peak_element = your_list[i]
            return peak_element
    for i in range(0, len_list, 2):
        if i == 0 or i == len_list - 1:
            continue
        if your_list[i - 1] < your_list[i] and your_list[i + 1] < your_list[i]:
            peak_element = your_list[i]
            return peak_element
    if your_list[0] >= your_list[len_list - 1]:
        peak_element = your_list[0]
    else:
        peak_element = your_list[len_list - 1]
    return peak_element
