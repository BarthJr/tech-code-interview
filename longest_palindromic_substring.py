# Write a function that, given a string, returns its longest palindromic substring.
# A palindrome is defined as a string that is written the same forward and backward.
# Assume that there will only be one longest palindromic substring.

"""
>>> longestPalindromicSubstring('abaxyzzyxf')
'xyzzyx'
"""


def longestPalindromicSubstring(string):
    longest = [0, 1]
    for i in range(1, len(string)):
        odd = get_longest_palindrome(string, i - 1, i + 1)
        even = get_longest_palindrome(string, i - 1, i)
        potencial_longest = max(odd, even, key=lambda x: x[1] - x[0])
        longest = max(potencial_longest, longest, key=lambda x: x[1] - x[0])
    return string[longest[0]: longest[1]]


def get_longest_palindrome(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    return [left + 1, right]
