# Given an unsorted array of integers, find the length of longest increasing subsequence.
"""
>>> lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
4
>>> lengthOfLIS([-1, 3, 4, 5, 2, 2, 2, 2, 2])
4
>>> lengthOfLIS([])
0

"""
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    max_len = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                max_len[i] = max(max_len[i], max_len[j] + 1)
    return max(max_len)
