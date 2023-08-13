#!/usr/bin/python3
for tens in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("{} = 0x{:x}".format((tens * 10 + digit), (tens * 10 + digit)))
