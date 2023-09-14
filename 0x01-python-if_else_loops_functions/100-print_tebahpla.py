#!/usr/bin/python3
_ascii = 65
for counter in range(0, 26):
    if _ascii % 2 == 0:
        print("{:c}".format(_ascii + 32), end="")
    else:
        print("{:c}".format(_ascii), end="")
    _ascii += 1
