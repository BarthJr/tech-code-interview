# You are given an array of arrays. Each subarray in this array holds two integer values and represents an item;
# the first integer is the item's value, and the second integer is the item's weight.
# You are also given an integer representing the maximum capacity of a knapsack that you have.
# Your goal is to fit items in your knapsack, all the while maximizing their combined value.
# Note that the sum of the weights of the items that you pick cannot exceed the knapsack's capacity.
# Write a function that returns the maximized combined value of the items that you should pick,
# as well as an array of the indices of each item picked.
# Assume that there will only be one combination of items that maximizes the total value in the knapsack.

"""
>>> knapsackProblem([[1,2],[4,3],[5,6],[6,7]], 10)
[10, [1, 3]]
"""


def knapsackProblem(items, capacity):
    dp = [[0 for _ in range(0, capacity + 1)] for _ in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        weight = items[i - 1][1]
        value = items[i - 1][0]
        for j in range(0, capacity + 1):
            if weight <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]
    return [dp[-1][-1], get_choosen_items(items, dp)]


def get_choosen_items(items, dp):
    result = []
    i = len(dp) - 1
    j = len(dp[0]) - 1
    while i > 0:
        if dp[i - 1][j] == dp[i][j]:
            i -= 1
        else:
            result.append(i - 1)
            j -= items[i - 1][1]
            i -= 1
        if j == 1:
            break
    return list(reversed(result))
