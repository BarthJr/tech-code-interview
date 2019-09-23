# Given an non-empty array of integers, write a function that returns an array of length 2.
# The first element in the output array should be an integer value representing the greatest sum that can be generated
# from a strictly-increasing subsequence in the array.
# The second element should be an array of the numbers in that subsequence.
# A subsequence is defined as a set of numbers that are not necessarily adjacent but
# that are in the same order as they appear in the array.
# Assume that there will only be one increasing subsequence with the greatest sum.

"""
>>> maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30])
[110, [10, 20, 30, 50]]
>>> maxSumIncreasingSubsequence([8, 12, 2, 3, 15, 5, 7])
[35, [8, 12, 15]]
"""


def maxSumIncreasingSubsequence(array):
    sums = array[:]
    sequences = [None] * (len(array))
    for i in range(len(array)):
        for j in range(0, i):
            if array[j] < array[i]:
                if sums[j] + array[i] > sums[i]:
                    sums[i] = sums[j] + array[i]
                    sequences[i] = j
    max_value = max(sums)
    max_idx = sums.index(max_value)
    sequence_path = get_sequence(array, sequences, max_idx)
    return [max_value, sequence_path]


def get_sequence(array, sequences, max_idx):
    result = []
    num = max_idx
    while num is not None:
        result.append(array[num])
        num = sequences[num]
    return list(reversed(result))
