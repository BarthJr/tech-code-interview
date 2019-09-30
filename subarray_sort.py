# Write a function that takes in an array of integers of length at least 2.
# The function should return an array of the starting and ending indices of the smallest subarray in the input array
# that needs to be sorted in place in order for the entire input array to be sorted.
# If the input array is already sorted, the function should return [-1, -1].

"""
>>> subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
[3, 9]
"""


def subarraySort(array):
    min_unsorted_value = float('inf')
    max_unsorted_value = float('-inf')
    for i, num in enumerate(array):
        if is_unsorted_array(i, num, array):
            min_unsorted_value = min(min_unsorted_value, num)
            max_unsorted_value = max(max_unsorted_value, num)

    if min_unsorted_value == float('inf'):
        return [-1, -1]

    min_idx = 0
    while min_unsorted_value >= array[min_idx]:
        min_idx += 1

    max_idx = len(array) - 1
    while max_unsorted_value <= array[max_idx]:
        max_idx -= 1

    return [min_idx, max_idx]


def is_unsorted_array(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]
