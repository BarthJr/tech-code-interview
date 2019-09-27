# Write a function that takes in an array of unique integers and returns an array of all permutations of those integers.
# If the input array is empty, your function should return an empty array.

"""
>>> getPermutations([1, 2, 3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
>>> getPermutations([])
[]
"""


def getPermutations(array):
    permutations = []
    getPermutationsHelper(array, 0, permutations)
    return permutations


def getPermutationsHelper(array, i, permutations):
    if i == len(array) - 1:
        return permutations.append(array[:])
    for j in range(i, len(array)):
        array[i], array[j] = array[j], array[i]
        getPermutationsHelper(array, i + 1, permutations)
        array[i], array[j] = array[j], array[i]
