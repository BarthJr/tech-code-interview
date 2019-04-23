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
    RED, WHITE, BLUE = 0, 1, 2
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == RED:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == WHITE:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    nums[:] = nums
