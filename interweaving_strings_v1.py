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


# O(2^(n + m)) time | O(n + m) space
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    return interweavingStringsRecursive(one, two, three, 0, 0, 0)


def interweavingStringsRecursive(one, two, three, i, j, k):
    if len(three) == k:
        return True

    if i < len(one) and one[i] == three[k]:
        if interweavingStringsRecursive(one, two, three, i + 1, j, k + 1):
            return True

    if j < len(two) and two[j] == three[k]:
        return interweavingStringsRecursive(one, two, three, i, j + 1, k + 1)

    return False
