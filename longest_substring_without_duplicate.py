# Write a function that takes in a string and that returns its longest substring without duplicate characters.
# Assume that there will only be one longest substring without duplication.

"""
>>> longestSubstringWithoutDuplication('clementisacap')
'mentisac'
"""


def longestSubstringWithoutDuplication(string):
    chars = {}
    start_idx = 0
    longest = [0, 1]
    for i, char in enumerate(string):
        if char in chars:
            start_idx = max(start_idx, chars[char] + 1)
        potential_longest = [start_idx, i + 1]
        longest = max(longest, potential_longest, key=lambda x: x[1] - x[0])
        chars[char] = i

    return string[longest[0]:longest[1]]
