# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

"""
>>> Solution().search([-1,0,3,5,9,12], 12)
5
>>> Solution().search([-1,0,3,5,9,12], 10)
-1
>>> Solution().search([5], 5)
0
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startIdx = 0
        endIdx = len(nums) - 1
        while startIdx <= endIdx:
            midIdx = (startIdx + endIdx) // 2
            if nums[midIdx] == target:
                return midIdx
            elif nums[midIdx] < target:
                startIdx = midIdx + 1
            else:
                endIdx = midIdx - 1
        return -1
