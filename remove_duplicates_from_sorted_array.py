# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given a sorted array nums,
# remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List
from unittest import TestCase


def removeDuplicates(nums: List[int]) -> int:
    if nums:
        elem = nums[0]
        length = 1
        for i in range(1, len(nums)):
            if elem != nums[i]:
                elem = nums[i]
                nums[length] = elem
                length += 1
        return length
    return 0


class TestRemoveDuplicates(TestCase):
    def test_empty(self):
        self.assertEqual(0, removeDuplicates([]))

    def test_simple_case(self):
        self.assertEqual(5, removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
