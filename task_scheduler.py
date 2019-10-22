# https://leetcode.com/problems/task-scheduler/

# Given a char array representing tasks CPU need to do.
# It contains capital letters A to Z where different letters represent different tasks.
# Tasks could be done without original order. Each task could be done in one interval.
# For each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two same tasks,
# there must be at least n intervals that CPU are doing different tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to finish all the given tasks.

"""
>>> Solution().leastInterval(tasks = ["A", "A", "A", "B", "B", "B"], n = 2)
8
"""
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = list(-1 * x for x in Counter(tasks).values())
        heapq.heapify(max_heap)
        cycles = 0
        while max_heap:
            temp = []
            for i in range(n):
                if max_heap:
                    temp.append(-1 * heapq.heappop(max_heap))
            for i in range(len(temp)):
                if temp[i] - 1 > 0:
                    temp[i] -= 1
                    max_heap.append(-1 * temp[i])
            cycles += n + 1 if max_heap else len(temp)
        return cycles
