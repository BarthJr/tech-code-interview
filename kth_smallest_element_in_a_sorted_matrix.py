# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
"""
>>> matrix = [[1, 2],[1 ,3]]
>>> k = 1
>>> kthSmallest(matrix, k)
1

>>> matrix = [[1, 2],[1 ,3]]
>>> k = 2
>>> kthSmallest(matrix, k)
1

>>> matrix = [[1, 5, 9],[10 ,11, 12], [12, 13, 15]]
>>> k = 8
>>> kthSmallest(matrix, k)
13

>>> matrix = [[1,3,5],[6,7,12],[11,14,14]]
>>> k = 4
>>> kthSmallest(matrix, k)
6

>>> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
>>> k = 20
>>> kthSmallest(matrix, k)
21
"""
from itertools import chain
from typing import List


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    return sorted(chain(*matrix))[k - 1]
