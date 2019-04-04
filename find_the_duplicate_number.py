# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
"""
>>> findDuplicate([1, 3, 4, 2, 2])
2
>>> findDuplicate([3, 1, 3, 4, 2])
3
>>> findDuplicate([2, 2, 2, 2, 2])
2
>>> findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1])
9
"""
from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow, fast, to_find = nums[0], nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            while to_find != slow:
                to_find = nums[to_find]
                slow = nums[slow]
            return to_find
