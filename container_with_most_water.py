# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

"""
>>> max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
49
>>> max_area([2, 1])
1
"""
from typing import List


def max_area(height: List[int]) -> int:
    low = 0
    high = len(height) - 1
    biggest_area = 0
    while low < high:
        length = (high - low)
        width = min(height[low], height[high])
        area = length * width
        biggest_area = max(biggest_area, area)
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1
    return biggest_area
