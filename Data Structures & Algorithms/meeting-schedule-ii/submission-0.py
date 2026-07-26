"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        res = 1
        prev_end = intervals[0].end
        for inter in intervals[1:]:
            if inter.start < prev_end:
                prev_end = min(inter.end, prev_end)
                res += 1
            else:
                prev_end = inter.end
        return res
