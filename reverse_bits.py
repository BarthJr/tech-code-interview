# https://leetcode.com/problems/reverse-bits/
# Reverse bits of a given 32 bits unsigned integer.
from unittest import TestCase


def reverse_bits(n: int) -> int:
    int_to_bin = '{0:032b}'.format(n)
    bin_reversed = int_to_bin[::-1]
    return int(bin_reversed, 2)


class TestReverseBits(TestCase):
    def test_simple_case(self):
        """
        input in binary is: 00000010100101000001111010011100
        return in binary must be: 00111001011110000010100101000000
        """
        self.assertEqual(964176192, reverse_bits(43261596))
