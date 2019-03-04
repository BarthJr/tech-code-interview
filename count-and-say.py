# https://leetcode.com/problems/count-and-say/

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

from unittest import TestCase


def countAndSay(n: int) -> str:
    return _count_and_say(n - 1)


def _count_and_say(count):
    if count == 0:
        return '1'
    else:
        result = []
        n = _count_and_say(count - 1)
        previous = n[0]
        count = 1
        for i in range(1, len(n)):
            if previous != n[i]:
                result.extend([str(count), previous])
                count = 1
                previous = n[i]
            else:
                count += 1
        result.extend([str(count), previous])
    return ''.join(result)


class TestCountAndSay(TestCase):
    def test_should_return_1_given_1(self):
        self.assertEqual('1', countAndSay(1))

    def test_should_return_11_given_2(self):
        self.assertEqual('11', countAndSay(2))

    def test_should_return_21_given_3(self):
        self.assertEqual('21', countAndSay(3))

    def test_should_return_1211_given_4(self):
        self.assertEqual('1211', countAndSay(4))

    def test_should_return_111221_given_5(self):
        self.assertEqual('111221', countAndSay(5))
