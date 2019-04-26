# Given a positive integer n,
# find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

"""
>>> numSquares(12)
3
>>> numSquares(13)
2
>>> numSquares(0)
0
>>> numSquares(1)
1
"""

_dp = [0]


def numSquares(n: int) -> int:
    dp = _dp
    while len(dp) <= n:
        aux = dp[-1]
        i = 1
        while i * i <= len(dp):
            aux = min(aux, dp[-i * i])
            i += 1
        dp.append(aux + 1)
    return dp[n]
