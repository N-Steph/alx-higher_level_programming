#!/usr/bin/python3
for tens in range(0, 10):
    if (tens > 8):
        break
    for digit in range(0, 10):
        if digit > tens:
            if (tens == 8 and digit == 9):
                print("{}{}".format(tens, digit))
                break
            print("{}{}, ".format(tens, digit), end='')
