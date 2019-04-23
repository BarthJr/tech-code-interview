# Given an array with n objects colored red, white or blue,
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
# Examples:
"""
>>> nums = [2, 0, 2, 1, 1, 0]
>>> sort_colors(nums)
>>> nums
[0, 0, 1, 1, 2, 2]
>>> nums = [2, 0]
>>> sort_colors(nums)
>>> nums
[0, 2]
>>> nums = [2]
>>> sort_colors(nums)
>>> nums
[2]
"""
from typing import List


def sort_colors(nums: List[int]) -> None:
    array = [0, 0, 0]
    for num in nums:
        array[num] += 1

    pos = 0
    for i, count in enumerate(array):
        for j in range(count):
            nums[pos] = i
            pos += 1

    nums[:] = nums
