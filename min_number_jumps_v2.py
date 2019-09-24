# You are given a non-empty array of integers. Each element represents the maximum number of steps you can take forward.
# For example, if the element at index 1 is 3, you can go from index 1 to index 2, 3, or 4.
# Write a function that returns the minimum number of jumps needed to reach the final index.
# Note that jumping from index i to index i + x always constitutes 1 jump, no matter how large x is.

"""
>>> minNumberOfJumps([1, 2, 1])
2
>>> minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])
4
"""


def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    max_reach = array[0]
    steps = array[0]
    jumps = 0
    for i in range(1, len(array) - 1):
        max_reach = max(max_reach, array[i] + i)
        steps -= 1
        if not steps:
            jumps += 1
            steps = max_reach - i
    return jumps + 1
