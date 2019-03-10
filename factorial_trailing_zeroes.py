# Given an integer n, return the number of trailing zeroes in n!.

from unittest import TestCase


def trailingZeroes(n: int) -> int:
    result = 0
    while n > 0:
        n //= 5
        result += n
    return result


class TestTrailingZeroes(TestCase):
    def test_simple_case(self):
        self.assertEqual(0, trailingZeroes(3))

    def test_should_return_2_given_10(self):
        self.assertEqual(2, trailingZeroes(10))

    def test_with_big_input(self):
        self.assertEqual(452137076, trailingZeroes(1808548329))
