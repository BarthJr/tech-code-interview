# Write a function that takes an unsigned integer
# and return the number of '1' bits it has(also known as the Hamming weight).
from unittest import TestCase


def hammingWeight(n):
    count = 0
    while n:
        count += 1
        n &= (n - 1)
    return count


class TestHammingWeight(TestCase):
    def test_should_return_3_given_11(self):
        self.assertEqual(3, hammingWeight(11))

    def test_should_return_1_given_128(self):
        self.assertEqual(1, hammingWeight(128))

    def test_should_return_31_given_4294967293(self):
        self.assertEqual(31, hammingWeight(4294967293))
