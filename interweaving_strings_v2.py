#   Write a function that takes in three strings and returns a boolean
#   representing whether the third string can be formed by interweaving the first
#   two strings.
#
#   To interweave strings means to merge them by alternating their letters without
#   any specific pattern. For instance, the strings 'abc' and '123' can be interwoven
#   as 'a1b2c3', as 'abc123', and as 'ab1c23' (this list is nonexaustive).
#
#   Letters within a string must maintain their relative ordering in the
#   interwoven string.

"""
>>> interweavingStrings('a', 'b', 'ab')
True
>>> interweavingStrings('a', 'b', 'ba')
True
>>> interweavingStrings('a', 'b', 'ac')
False
>>> interweavingStrings('abc', 'def', 'abcdef')
True
>>> interweavingStrings('abc', 'def', 'adbecf')
True
>>> interweavingStrings('aabcc', 'dbbca', 'aadbbcbcac')
True
"""


# O(n*m) time | O(n*m) space
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    dp = [[None for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]

    return interweavingStringsRecursive(one, two, three, 0, 0, 0, dp)


def interweavingStringsRecursive(one, two, three, i, j, k, dp):
    if dp[i][j]:
        return dp[i][j]

    if len(three) == k:
        dp[i][j] = True
        return dp[i][j]

    if i < len(one) and one[i] == three[k]:
        dp[i][j] = interweavingStringsRecursive(one, two, three, i + 1, j, k + 1, dp)
        if dp[i][j]:
            return dp[i][j]

    if j < len(two) and two[j] == three[k]:
        dp[i][j] = interweavingStringsRecursive(one, two, three, i, j + 1, k + 1, dp)
        return dp[i][j]

    dp[i][j] = False
    return dp[i][j]
