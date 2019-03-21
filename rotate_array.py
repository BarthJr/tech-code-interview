# Given an array, rotate the array to the right by k steps, where k is non-negative.

from typing import List
from unittest import TestCase


def rotate(nums: List[int], steps: int) -> None:
    diff = len(nums) - steps
    nums[:] = nums[diff:] + nums[:diff]


class TestRotate(TestCase):
    def test_simple_case(self):
        lst, k = [1, 2, 3, 4, 5, 6, 7], 3
        rotate(lst, k)
        self.assertListEqual([5, 6, 7, 1, 2, 3, 4], lst)

    def test_empty_list(self):
        lst, k = [], 1
        rotate(lst, k)
        self.assertListEqual([], lst)

    def test_list_with_one_element_should_become_the_own_list(self):
        lst, k = [1], 1
        rotate(lst, k)
        self.assertListEqual([1], lst)

    def test_list_with_two_elements_and_1_step_should_become_the_reverse_list(self):
        lst, k = [1, 2], 1
        rotate(lst, k)
        self.assertListEqual([2, 1], lst)

    def test_list_with_two_elements_and_2_steps_should_become_the_own_list(self):
        lst, k = [1, 2], 2
        rotate(lst, k)
        self.assertListEqual([1, 2], lst)
