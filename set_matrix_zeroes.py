# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
"""
>>> matrix = [
...             [1, 1, 1],
...             [1, 0, 1],
...             [1, 1, 1]
...          ]
>>> set_zeroes(matrix)
>>> matrix
[[1, 0, 1], [0, 0, 0], [1, 0, 1]]

>>> matrix = [
...             [0, 1, 2, 0],
...             [3, 4, 5, 2],
...             [1, 3, 1, 5],
...          ]
>>> set_zeroes(matrix)
>>> matrix
[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

>>> matrix = []
>>> set_zeroes(matrix)
>>> matrix
[]

"""
from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    mark_zeroes = set()
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == 0:
                mark_zeroes.add((i, j))
    change_matrix(mark_zeroes, matrix)


def change_matrix(mark_zeroes, matrix):
    for mark in mark_zeroes:
        idx_i, idx_j = mark
        for j in range(len(matrix[0])):
            matrix[idx_i][j] = 0
        for i in range(len(matrix)):
            matrix[i][idx_j] = 0
