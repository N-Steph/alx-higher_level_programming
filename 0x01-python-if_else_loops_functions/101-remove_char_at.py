#!/usr/bin/python3
def remove_char_at(_str, n):
    if type(_str) is not str:
        return
    if len(_str) <= n:
        return _str
    copy_str = ""
    counter = 0
    for char in _str:
        if counter != n:
            copy_str = copy_str + char
        counter += 1
    return copy_str
