# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Given two arrays, write a function to compute their intersection.

from unittest import TestCase
from bisect import bisect_left


def intersect(nums1, nums2):
    """
    :param nums1: List[int]
    :param nums2: List[int]
    :return: List[int]
    """

    nums2.sort()
    result = []
    for num in nums1:
        index_founded = bisect_left(nums2, num)
        if index_founded != len(nums2) and nums2[index_founded] == num:
            result.append(num)
            nums2.remove(num)
    return result


class TestIntersect(TestCase):
    def test_with_repeated_number_both_lists(self):
        self.assertEqual([2, 2], intersect([1, 2, 2, 1], [2, 2]))

    def test_with_multiple_repeated_numbers_both_lists(self):
        self.assertEqual([4, 9], intersect([4, 9, 5], [9, 4, 9, 8, 4]))

    def test_list_with_repeated_numbers_matching_to_one_number_in_other_list(self):
        self.assertEqual([1], intersect([1, 1], [1, 2]))

    def test_list_with_repeated_numbers_matching_to_a_list_with_unique_number(self):
        self.assertEqual([2], intersect([1, 2, 2, 1], [2]))
