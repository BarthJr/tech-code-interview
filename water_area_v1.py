# You are given an array of integers. Each non-zero integer represents the height of a pillar of width 1.
# Imagine water being poured over all of the pillars and return the surface area of the water trapped
# between the pillars viewed from the front. Note that spilled water should be ignored.

"""
>>> waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
48
"""


def waterArea(heights):
    left_array = [0 for _ in heights]
    max_height = 0

    for i in range(len(heights)):
        left_array[i] = max_height
        max_height = max(heights[i], max_height)

    right_array = [0 for _ in heights]
    max_height = 0
    for i in reversed(range(len(heights))):
        right_array[i] = max_height
        max_height = max(heights[i], max_height)

    result = [0 for _ in heights]

    for i in range(len(result)):
        min_height = min(left_array[i], right_array[i])
        if heights[i] < min_height:
            result[i] = min_height - heights[i]
        else:
            result[i] = 0

    return sum(result)
