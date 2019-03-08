# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List
from unittest import TestCase


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''
    strs.sort()
    min_strs, max_strs = strs[0], strs[-1]
    for i, letter in enumerate(min_strs):
        if max_strs[i] != letter:
            return min_strs[:i]
    return min_strs


class TestsLongestCommonPrefix(TestCase):
    def test_empty_list(self):
        self.assertEqual('', longestCommonPrefix([]))

    def test_with_one_element_in_list(self):
        self.assertEqual('flower', longestCommonPrefix(["flower"]))

    def test_simple_case(self):
        self.assertEqual('fl', longestCommonPrefix(["flower", "flow", "flight"]))

    def test_with_no_common_prefix(self):
        self.assertEqual('', longestCommonPrefix(["dog", "racecar", "car"]))

    def test_with_common_prefix(self):
        self.assertEqual('a', longestCommonPrefix(["abcde", "abcdeea", "abc", "adbc"]))
