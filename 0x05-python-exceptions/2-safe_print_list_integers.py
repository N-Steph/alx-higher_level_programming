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
        except Exception:
            i += 1
            pass
        else:
            counter += 1
            i += 1
    return (counter)
