# Given an m x n matrix, return all elements of the matrix in spiral order.

# Examples:
"""
>>> spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
[1, 2, 3, 6, 9, 8, 7, 4, 5]
>>> spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
>>> spiralOrder([[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> spiralOrder([[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    startRow = 0
    endRow = len(matrix)
    startCol = 0
    endCol = len(matrix[0])

    while startRow < endRow and startCol < endCol:
        for col in range(startCol, endCol):
            result.append(matrix[startRow][col])
        startRow += 1

        for row in range(startRow, endRow):
            result.append(matrix[row][endCol - 1])
        endCol -= 1

        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            result.append(matrix[endRow - 1][col])
        endRow -= 1

        for row in reversed(range(startRow, endRow)):
            if startCol == endCol:
                break
            result.append(matrix[row][startCol])
        startCol += 1

    return result
