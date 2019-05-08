"""
>>> w = [
...  [1,   4,  7, 11, 15],
...  [2,   5,  8, 12, 19],
...  [3,   6,  9, 16, 22],
...  [10, 13, 14, 17, 24],
...  [18, 21, 23, 26, 30]
... ]
>>> searchMatrix(w, 5)
True

>>> searchMatrix([[]], 5)
False

"""


def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    len_row = len(matrix[0]) - 1
    for row in matrix:
        find = binary_search(row, target, len_row)
        if row[find] == target:
            return True
    return False


def binary_search(row, target, right):
    left = 0
    while left < right - 1:
        mid = (left + right) // 2
        if target < row[mid]:
            right = mid
        else:
            left = mid

    if target < row[right]:
        return left
    return right
