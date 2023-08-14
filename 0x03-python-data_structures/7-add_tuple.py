#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds 2 tuples.
    Add the first element of tuple_a with
    first element of tuple_b and
    second element of tuple_a with second
    element of tuple_b

    Return a tuple of the two integers obtain from the addition
    """
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        tuple_add = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        tuple_add = tuple_a[0] + tuple_b[0], 0 + tuple_b[1]
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        tuple_add = tuple_a[0] + tuple_b[0],  tuple_a[1] + 0
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        tuple_add = tuple_a[0] + tuple_b[0], 0
    elif len(tuple_a) == 0 and len(tuple_b) == 1:
        tuple_add = tuple_b[0], 0
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        tuple_add = tuple_a[0], 0
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        tuple_add = tuple_a[0], tuple_a[1]
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        tuple_add = tuple_b[0], tuple_b[1]
    else:
        tuple_add = 0, 0
    return tuple_add
