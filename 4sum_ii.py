# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
# Example:
"""
>>> A = [ 1, 2]
>>> B = [-2,-1]
>>> C = [-1, 2]
>>> D = [ 0, 2]
>>> four_sum_count(A, B, C, D)
2
"""
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

from typing import List


def four_sum_count(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    hash_table, count = {}, 0
    for i in A:
        for j in B:
            hash_table[i + j] = hash_table.get(i + j, 0) + 1

    for i in C:
        for j in D:
            count += hash_table.get(-i - j, 0)
    return count
