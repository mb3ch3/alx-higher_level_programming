#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_tmp = []
    for i in range(len(matrix)):
        new = []
        for j in range(len(matrix[0])):
            new.append(matrix[i][j] ** 2)
            matrix_tmp.append(new)
    return matrix_tmp
