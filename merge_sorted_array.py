# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space
# (size that is greater or equal to m + n) to hold additional elements from nums2.

import bisect
from typing import List
from unittest import TestCase


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i in range(n):
        nums1.pop()
    for num in nums2:
        bisect.insort_left(nums1, num)


class TestMerge(TestCase):
    def test_with_2_empty_lists(self):
        nums1 = []
        nums2 = []
        merge(nums1, 0, nums2, len(nums2))
        self.assertEqual([], nums1)

    def test_with_first_list_empty(self):
        nums1 = [0]
        nums2 = [1]
        merge(nums1, 0, nums2, len(nums2))
        self.assertEqual([1], nums1)

    def test_with_second_list_empty(self):
        nums1 = [1]
        nums2 = []
        merge(nums1, 1, nums2, len(nums2))
        self.assertEqual([1], nums1)

    def test_with_zeros_in_middle_of_first_list(self):
        nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0, 0]
        nums2 = [0, 1, 2, 2]
        merge(nums1, 6, nums2, len(nums2))
        self.assertEqual([-1, 0, 0, 0, 1, 2, 2, 3, 3, 3], nums1)
