# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

"""
>>> sherlockAndAnagrams("abba")
4
>>> sherlockAndAnagrams("kkkk")
10
>>> sherlockAndAnagrams("abcd")
0
>>> sherlockAndAnagrams("ifailuhkqq")
3
"""


def sherlockAndAnagrams(s):
    numberAnagrams = 0
    hashMap = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            toFind = ''.join(sorted(s[i:j]))
            hashMap[toFind] = hashMap.get(toFind, 0) + 1

    for value in hashMap.values():
        numberAnagrams += (value * (value - 1)) // 2
    return numberAnagrams
