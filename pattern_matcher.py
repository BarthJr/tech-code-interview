# You are given two non-empty strings. The first one is a pattern consisting of only "x"s and / or "y"s;
# the other one is a normal string of alphanumeric characters.
# Write a function that checks whether or not the normal string matches the pattern.
# A string S0 is said to match a pattern if replacing all "x"s in the pattern with some string S1
# and replacing all "y"s in the pattern with some string S2 yields the same string S0.
# If the input string does not match the input pattern, return an empty array;
# otherwise, return an array holding the representations of "x" and "y" in the normal string, in that order.
# If the pattern does not contain any "x"s or "y"s,
# the respective letter should be represented by an empty string in the final array that you return.
# Assume that there will never be more than one pair of strings S1 and S2 that appropriately represent "x" and "y"
# in the input string.

"""
>>> patternMatcher('xxyxxy', 'gogopowerrangergogopowerranger')
['go', 'powerranger']
"""

from collections import Counter


def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []

    new_pattern = get_new_pattern(pattern)
    did_switch = new_pattern[0] != pattern[0]
    counts = {'x': 0, 'y': 0}
    counts.update(dict(Counter(new_pattern)))
    first_y_pos = new_pattern.index('y') if 'y' in new_pattern else None

    if counts['y'] != 0:
        for len_x in range(1, len(string)):
            len_y = (len(string) - len_x * counts['x']) / counts['y']
            if len_y <= 0 or len_y % 1 != 0:
                continue
            len_y = int(len_y)
            y_idx = first_y_pos * len_x
            x = string[:len_x]
            y = string[y_idx:y_idx + len_y]
            potential_match = map(lambda char: x if char == 'x' else y, new_pattern)
            if string == ''.join(potential_match):
                return [x, y] if not did_switch else [y, x]
    else:
        len_x = len(string) / counts['x']
        if len_x % 1 == 0:
            len_x = int(len_x)
            x = string[:len_x]
            potential_match = map(lambda char: x, new_pattern)
            if string == ''.join(potential_match):
                return [x, ''] if not did_switch else ['', x]

    return []


def get_new_pattern(pattern):
    pattern_letters = list(pattern)
    if pattern[0] == 'x':
        return pattern_letters
    return list(map(lambda char: 'x' if char == 'y' else 'y', pattern_letters))
