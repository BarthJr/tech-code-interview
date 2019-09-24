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
    jumps = [float('inf') for _ in array]
    jumps[0] = 0
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[-1]
