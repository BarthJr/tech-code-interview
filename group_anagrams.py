# Given an array of strings, group anagrams together.
#
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.
"""
>>> groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dct = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in dct:
            dct[sorted_s].append(s)
        else:
            dct[sorted_s] = [s]
    result = [value for value in dct.values()]
    return result
