#!/usr/bin/python3
_ascii = 122
for counter in range(0, 26):
    print("{:c}".format(_ascii - 32 if _ascii % 2 != 0 else _ascii), end="")
    _ascii -= 1
