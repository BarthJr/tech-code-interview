# https://www.lintcode.com/problem/meeting-rooms-ii/description

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.

"""
>>> minMeetingRooms([Interval(5, 10), Interval(15, 20), Interval(0, 30)])
2
>>> minMeetingRooms([Interval(7, 10), Interval(2, 4)])
1
"""

import heapq


class Interval:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end


def minMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda interval: interval.start)
    first_interval = intervals[0]
    min_heap = [first_interval.end]
    for i in range(1, len(intervals)):
        current = intervals[i]
        if current.start >= min_heap[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, current.end)

    return len(min_heap)
