# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.

"""
>>> find_peak_element([1, 2, 3, 1])
2
>>> find_peak_element([1, 2, 1, 3, 5, 6, 4])
1
>>> find_peak_element([2])
0
>>> find_peak_element([1, 3])
1
>>> find_peak_element([4, 2])
0

"""

from typing import List


def find_peak_element(nums: List[int]) -> int:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return i
    return len(nums) - 1
