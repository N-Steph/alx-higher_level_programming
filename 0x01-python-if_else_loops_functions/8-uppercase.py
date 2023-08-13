#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    return False


def uppercase(str):
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in str:
        if islower(letter):
            index = ord(letter) - 97
            letter = upperCase[index]
        print("{}".format(letter), end='')

    print()
