"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda inter: inter.start)
        left = intervals[0]
        for r in range(1, len(intervals)):
            if left.end <= intervals[r].start:              
                left = intervals[r]
            else:
                return False
        return True
