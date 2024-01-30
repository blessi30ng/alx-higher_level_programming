#!/usr/bin/python3

def matrix_divided(matrix, div):
    """divides matrix by scalar integer, rounded to two decimal places"""
    import decimal
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_msg)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err_msg)
        len_rows.append(len(row))
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(err_msg)
        row_count += 1
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda row: list(map(lambda x: round(x/div, 2), row)), matrix))
