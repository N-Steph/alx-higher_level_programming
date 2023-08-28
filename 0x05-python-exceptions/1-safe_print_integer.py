#!/usr/bin/python3
def safe_print_integer(value):
    """
    Function that prints an integer with '{:d}".format()
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return (False)
    else:
        return (True)
