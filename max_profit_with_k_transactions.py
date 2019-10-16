# You are given an array of integers representing the prices of a single stock on various days
# (each index in the array represents a different day). You are also given an integer k,
# which represents the number of transactions you are allowed to make.
# One transaction consists of buying the stock on a given day and selling it on another, later day.
# Write a function that returns the maximum profit that you can make buying and selling the stock,
# given k transactions. Note that you can only hold 1 share of the stock at a time; in other words,
# you cannot buy more than 1 share of the stock on any given day,
# and you cannot buy a share of the stock if you are still holding another share.

# Sample input: [5, 11, 3, 50, 60, 90], 2
# Sample output: 93 (Buy: 5, Sell: 11; Buy: 3, Sell: 90)
"""
>>> maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2)
93
"""


def maxProfitWithKTransactions(prices, k):
    if not prices:
        return 0

    profits = [[0 for j in prices] for i in range(k + 1)]

    for i in range(1, k + 1):
        max_previous_profit = float('-inf')
        for j in range(1, len(prices)):
            max_previous_profit = max(max_previous_profit, profits[i - 1][j - 1] - prices[j - 1])
            profits[i][j] = max(profits[i][j - 1], prices[j] + max_previous_profit)

    return profits[-1][-1]
