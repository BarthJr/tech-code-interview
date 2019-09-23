# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array
# of all these triplets. The numbers in each triplet should be ordered in ascending order,
# and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
# If no three numbers sum up to the target sum, the function should return an empty array.

"""
>>> threeNumberSum([1, 3, 2, 5,-1], 6)
[[-1, 2, 5], [1, 2, 3]]
>>> threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""


def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < targetSum:
                left += 1
            elif current_sum > targetSum:
                right -= 1
    return result
