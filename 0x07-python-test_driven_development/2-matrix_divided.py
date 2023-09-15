#!/usr/bin/python3
"""
This module defines a number of functions used
for the successfule division of all elements of
a matrix
"""


def handle_matrix_exception(matrix):
    """
    Check whether the matrix is in the appropriate form
    in order to perform the division of its elements
    """
    data_type = [int, float]
    _exception = TypeError("matrix must be a matrix "
                           "(list of lists) of integers/floats")

    # Check if matrix and constituents are lists
    if type(matrix) is not list:
        raise _exception
    for _sub_list in matrix:
        if type(_sub_list) is not list:
            raise _exception

    row_size = len(matrix[0])
    # check if sub_list element of matrix are int/floats
    for _sub_list in matrix:
        for element in _sub_list:
            if type(element) not in data_type:
                raise _exception
    # Check if matrix has same row size
    for _sub_list in matrix:
        if len(_sub_list) != row_size:
            raise TypeError("Each row of the matrix must have the same size")


def handle_div_exception(div):
    """
    Checks whether the 'div' is an appropriate divisor
    """
    data_type = [int, float]

    # Check if div is int/float and different from 0
    if type(div) not in data_type:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


def matrix_divided(matrix=[[1]], div=1):
    """
    Performs the division of of all elements of 'matrix
    Returns a new matrix containgin the results of the
    division
    """
    handle_matrix_exception(matrix)
    handle_div_exception(div)
    # Dividing each element of the matrix
    div_matrix = list()
    for _sub_list in matrix:
        new_sub_list = []
        for element in _sub_list:
            new_sub_list.append(round(element / div, 2))
        div_matrix.append(new_sub_list)

    return div_matrix
