# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.

"""
>>> subsets([1, 2, 3])
[(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
"""

from itertools import combinations
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    for i in range(len(nums) + 1):
        result.extend(combinations(nums, i))
    return result
