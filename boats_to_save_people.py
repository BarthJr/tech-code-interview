# https://leetcode.com/problems/boats-to-save-people/

# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.
# (It is guaranteed each person can be carried by a boat.)

"""
>>> Solution().numRescueBoats([1, 2], 3)
1
>>> Solution().numRescueBoats([3, 2, 2, 1], 3)
3
>>> Solution().numRescueBoats([3, 5, 3, 4], 5)
4
"""
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        num_boats = 0
        first_person = 0
        last_person = len(people) - 1

        people.sort()
        while first_person <= last_person:
            if people[first_person] + people[last_person] <= limit:
                first_person += 1
                last_person -= 1
            else:
                last_person -= 1
            num_boats += 1

        return num_boats
