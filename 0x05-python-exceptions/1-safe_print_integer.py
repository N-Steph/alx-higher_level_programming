#!/usr/bin/python3
def safe_print_integer(value):
    """
    Function that prints an integer with '{:d}".format()
    Returns Ture if value correctly printed and false otherwise
    """
    try:
        print("{:d}".format(value))
    except:
        return (False)
    else:
        return (True)
