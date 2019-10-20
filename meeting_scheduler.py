# https://leetcode.com/problems/meeting-scheduler/

# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration,
# return the earliest time slot that works for both of them and is of duration duration.
#
# If there is no common time slot that satisfies the requirements, return an empty array.
#
# The format of a time slot is an array of two elements [start, end]
# representing an inclusive time range from start to end.
#
# It is guaranteed that no two availability slots of the same person intersect with each other.
# That is, for any two time slots [start1, end1] and [start2, end2] of the same person,
# either start1 > end2 or start2 > end1.

"""
>>> slots1 = [[10, 50], [60, 120], [140, 210]]
>>> slots2 = [[0, 15], [60, 70]]
>>> duration = 8
>>> Solution().minAvailableDuration(slots1, slots2, duration)
[60, 68]
>>> Solution().minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12)
[]
"""

import heapq
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots = [x for x in slots1 + slots2 if x[1] - x[0] >= duration]
        heapq.heapify(slots)

        while len(slots) > 1:
            current = heapq.heappop(slots)
            first = slots[0][0]
            if current[1] >= first + duration:
                return [first, first + duration]

        return []
