# https://leetcode.com/problems/reverse-integer/
from unittest import TestCase


def reverse(n: 'int') -> 'int':
    n = str(n)
    if str(n)[0] == '-':
        n = n[1:] + '-'
    reversed_number = int(''.join(reversed(n)))
    if -2 ** 31 <= reversed_number <= 2 ** 31 - 1:
        return reversed_number
    else:
        return 0


class Tests(TestCase):
    def test_positive_number(self):
        self.assertEqual(321, reverse(123))

    def test_negative_number(self):
        self.assertEqual(-321, reverse(-123))

    def test_number_ending_with_zero(self):
        self.assertEqual(21, reverse(120))
