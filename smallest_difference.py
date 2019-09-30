# Write a function that takes in two non-empty arrays of integers.
# The function should find the pair of numbers (one from the first array,
# one from the second array) whose absolute difference is closest to zero.
# The function should return an array containing these two numbers,
# with the number from the first array in the first position.
# Assume that there will only be one pair of numbers with the smallest difference.

"""
>>> smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
[28, 26]
"""


def smallestDifference(arrayOne, arrayTwo):
    array1 = sorted(arrayOne)
    array2 = sorted(arrayTwo)

    idx_one = 0
    idx_two = 0
    values = [None, None]
    diff = float('inf')

    while idx_one < len(array1) and idx_two < len(array2):
        value_one = array1[idx_one]
        value_two = array2[idx_two]
        if value_one < value_two:
            diff, values = update_diff_values(value_one, value_two, diff, values)
            idx_one += 1
        elif value_one > value_two:
            diff, values = update_diff_values(value_one, value_two, diff, values)
            idx_two += 1
        else:
            return [value_one, value_two]

    return values


def update_diff_values(value_one, value_two, diff, values):
    if abs(value_one - value_two) < diff:
        diff = abs(value_one - value_two)
        values = [value_one, value_two]

    return diff, values
