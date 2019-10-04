# https://leetcode.com/problems/decode-ways/

"""
>>> numDecodings('12')
2
>>> numDecodings('226')
3
"""


def numDecodings(s: str) -> int:
    dp = [0 for _ in range(len(s) + 1)]
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1
    for i in range(2, len(s) + 1):
        one_digit = s[i - 1:i]
        two_digits = s[i - 2:i]
        if one_digit >= '1':
            dp[i] += dp[i - 1]
        if '10' <= two_digits <= '26':
            dp[i] += dp[i - 2]

    return dp[len(s)]
