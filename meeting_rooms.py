# https://www.lintcode.com/problem/meeting-rooms/description

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.

"""
>>> Solution().canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)])
False
>>> Solution().canAttendMeetings([Interval(5, 8), Interval(9, 15)])
True
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True
