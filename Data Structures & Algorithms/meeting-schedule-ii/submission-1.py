"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])
        p_s, p_e = 0, 0
        res = 0
        cur = 0
        while p_s < len(intervals):
            if start[p_s] < end[p_e]:
                p_s += 1
                cur +=1
            else: # start[p_s] >= end[p_e]
                p_e += 1
                cur -= 1
            res = max(res, cur)
        return res
