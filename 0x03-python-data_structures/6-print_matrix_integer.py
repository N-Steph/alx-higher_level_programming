#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers
    """
    for row in matrix:
        i = 0
        for col_element in row:
            i += 1
            print("{:d}".format(col_element), end='')
            if i != len(row):
                print(" ", end='')
        print()
