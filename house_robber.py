# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

from typing import List
from unittest import TestCase


def rob(nums: List[int]) -> int:
    memo = [None] * (len(nums) + 1)
    return _rob(0, nums, memo)


def _rob(i, nums, memo):
    if i > len(nums) - 1:
        return 0
    else:
        if memo[i] is not None:
            return memo[i]
        result = max(nums[i] + _rob(i + 2, nums, memo), _rob(i + 1, nums, memo))
        memo[i] = result
        return result


class TestRob(TestCase):
    def test_with_empty_list(self):
        self.assertEqual(0, rob([]))

    def test_with_list_zeros(self):
        self.assertEqual(0, rob([0, 0, 0, 0]))

    def test_with_one_element(self):
        self.assertEqual(2, rob([2]))

    def test_with_two_elements_and_last_bigger(self):
        self.assertEqual(2, rob([1, 2]))

    def test_with_two_elements_and_first_bigger(self):
        self.assertEqual(2, rob([2, 1]))

    def test_if_not_return_max_profit_with_adjacent_houses(self):
        self.assertEqual(4, rob([1, 2, 3, 1]))
