# Given two strings, determine if they share a common substring. A substring may be as small as one character.

"""
>>> twoStrings('and', 'art')
'YES'
>>> twoStrings('be', 'cat')
'NO'
>>> twoStrings('hello', 'world')
'YES'
>>> twoStrings('hi', 'world')
'NO'
"""


def twoStrings(s1, s2):
    hashMap = {}
    for s in s1:
        hashMap[s] = hashMap.get(s, 0)
    for s in s2:
        if s in hashMap:
            return 'YES'
    return 'NO'
