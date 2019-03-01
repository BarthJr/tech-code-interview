# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

from typing import List
from unittest import TestCase


def maxSubArray(nums: List[int]) -> int:
    max_current = max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


class TestMaxSubArray(TestCase):
    def test_check_if_return_largest_sum_or_last_sum(self):
        self.assertEqual(6, maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_with_negative_and_positive_number_should_return_positive_number(self):
        self.assertEqual(1, maxSubArray([-2, 1]))

    def test_with_one_negative_number_should_return_the_negative_number(self):
        self.assertEqual(-2, maxSubArray([-2]))
