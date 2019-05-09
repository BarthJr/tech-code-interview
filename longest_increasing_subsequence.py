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
    tails = [0] * len(nums)
    larger = 0
    for num in nums:
        left, right = 0, larger
        while left != right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        tails[left] = num
        larger = max(left + 1, larger)
    return larger
