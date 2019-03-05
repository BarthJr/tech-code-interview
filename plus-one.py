# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

from typing import List
from unittest import TestCase


def plusOne(digits: List[int]) -> List[int]:
    number_plus_one = int(''.join((str(digit) for digit in digits))) + 1
    return [int(digit) for digit in str(number_plus_one)]


class TestPlusOne(TestCase):
    def test_should_return_124_given_123(self):
        self.assertListEqual([1, 2, 4], plusOne([1, 2, 3]))

    def test_should_return_10_given_9(self):
        self.assertListEqual([1, 0], plusOne([9]))

    def test_should_return_1000_given_999(self):
        self.assertListEqual([1, 0, 0, 0], plusOne([9, 9, 9]))
