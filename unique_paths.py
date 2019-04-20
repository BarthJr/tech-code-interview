# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Note: m and n will be at most 100.
"""
>>> uniquePaths(3, 2)
3
>>> uniquePaths(7, 3)
28
>>> uniquePaths(0, 0)
0
>>> uniquePaths(0, 2)
0
>>> uniquePaths(2, 0)
0
"""


def uniquePaths(m: int, n: int) -> int:
    if not m or not n:
        return 0
    dp = [[1 for col in range(n)] for row in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
