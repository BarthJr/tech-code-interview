# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
from itertools import chain
from typing import List
from unittest import TestCase


def getRow(rowIndex: int) -> List[int]:
    row = (1,)
    for num_row in range(rowIndex):
        row_with_left_zero = chain(range(1), row)
        row_with_right_zero = chain(row, range(1))
        row = tuple(x + y for x, y in zip(row_with_left_zero, row_with_right_zero))
    return list(row)


class TestGetRow(TestCase):
    def test_check_with_even_number(self):
        self.assertEqual([1, 4, 6, 4, 1], getRow(4))

    def test_check_with_odd_number(self):
        self.assertEqual([1, 3, 3, 1], getRow(3))

    def test_with_number_one_input(self):
        self.assertEqual([1, 1], getRow(1))

    def test_with_number_zero_input(self):
        self.assertEqual([1], getRow(0))
