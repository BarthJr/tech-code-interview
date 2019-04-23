# Design a data structure that supports all following operations in average O(1) time.
#
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements.
# Each element must have the same probability of being returned.
"""
>>> randomSet = RandomizedSet()
>>> randomSet.insert(1)
True
>>> randomSet.insert(3)
True
>>> randomSet.remove(2)
False
>>> randomSet.insert(2)
True
>>> randomSet.get_random()
1
>>> randomSet.remove(1)
True
>>> randomSet.insert(2)
False
>>> randomSet.get_random()
2
"""
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.idx_nums = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.idx_nums:
            self.nums.append(val)
            self.idx_nums[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.idx_nums:
            idx = self.idx_nums[val]
            last = self.nums[-1]
            self.nums[idx] = last
            self.idx_nums[last] = idx
            self.nums.pop()
            self.idx_nums.pop(val)
            return True
        return False

    def get_random(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
