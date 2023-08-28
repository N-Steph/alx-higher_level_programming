#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Functions that prints the first x elements of a list
    and only integers

    Returns the real number of integers printed
    """
    i = 0
    num_int = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            i += 1
            pass
        else:
            num_int += 1
            i += 1
    print()
    return (num_int)
