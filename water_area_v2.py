# You are given an array of integers. Each non-zero integer represents the height of a pillar of width 1.
# Imagine water being poured over all of the pillars and return the surface area of the water trapped
# between the pillars viewed from the front. Note that spilled water should be ignored.
# Refer to the first minute of the video explanation below for a visual example.

"""
>>> waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
48
"""


def waterArea(heights):
    result = [0 for _ in heights]
    maxes = result[:]
    max_height = 0
    for i in range(len(heights)):
        maxes[i] = max_height
        max_height = max(heights[i], max_height)

    max_height = 0
    for i in reversed(range(len(heights))):
        min_height = min(maxes[i], max_height)
        if heights[i] < min_height:
            result[i] = min_height - heights[i]
        else:
            result[i] = 0
        max_height = max(heights[i], max_height)
    return sum(result)
