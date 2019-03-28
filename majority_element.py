# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.

from typing import List
from unittest import TestCase


def majority_element(nums: List[int]) -> int:
    return sorted(nums)[len(nums) // 2]


class Tests(TestCase):
    def test_with_one_element_in_list(self):
        self.assertEqual(3, majority_element([3]))

    def test_with_odd_list(self):
        self.assertEqual(2, majority_element([2, 2, 1, 1, 1, 2, 2]))

    def test_with_even_list(self):
        self.assertEqual(2, majority_element([2, 2, 1, 1, 1, 2]))
