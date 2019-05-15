# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
#
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
"""
>>> increasing_triplet([1, 2, 3, 4, 5])
True
>>> increasing_triplet([5, 4, 3, 2, 1])
False
>>> increasing_triplet([5, 4, 3])
False
>>> increasing_triplet([1, 2, 3])
True
>>> increasing_triplet([3, 2, 4, 1, 5])
True
>>> increasing_triplet([])
False
>>> increasing_triplet([1, 1, 1])
False
>>> increasing_triplet([5, 1, 5, 5, 2, 5, 4])
True

"""
from typing import List


def increasing_triplet(nums: List[int]) -> bool:
    i = j = k = float('inf')
    for num in nums:
        if num <= i:
            i = num
        elif num <= j:
            j = num
        elif num <= k:
            return True
    return False
