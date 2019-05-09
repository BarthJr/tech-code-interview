# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
"""
>>> partition('aab')
[['aa', 'b'], ['a','a','b']]

"""
from typing import List


def partition(s: str) -> List[List[str]]:
    validDecompositions = []
    dfs(s, [], validDecompositions)
    return validDecompositions


def dfs(s, decompInProgress, validDecompositions):
    if not s:
        validDecompositions.append(decompInProgress)
    for i in range(1, len(s) + 1):
        if isPalindrome(s[:i]):
            dfs(s[i:], decompInProgress + [s[:i]], validDecompositions)


def isPalindrome(s):
    return s == s[::-1]
