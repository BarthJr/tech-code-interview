# Shuffle a set of numbers without duplicates.

# Your Solution object will be instantiated and called as such:
"""
>>> nums = [1, 2, 3]
>>> obj = Solution(nums)
>>> param_1 = obj.reset()
>>> param_2 = obj.shuffle()
"""
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.backup = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.backup
        self.backup = list(self.backup)
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums
