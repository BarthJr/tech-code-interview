# Write a function that takes in two strings and returns the minimum number of edit operations
# that need to be performed on the first string to obtain the second string.
# There are three edit operations: insertion of a character, deletion of a character, and substitution of a character
# for another.

"""
>>> levenshteinDistance('abc', 'abx')
1
>>> levenshteinDistance('abc', 'yabd')
2
"""


def levenshteinDistance(str1, str2):
    str1 = ' ' + str1
    str2 = ' ' + str2
    dp = [[float('inf')] * len(str2) for _ in range(len(str1))]
    dp[0] = [i for i in range(len(str2))]
    for i in range(1, len(str1)):
        dp[i][0] = i
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[-1][-1]
