class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (cur_sta, cur_end) in enumerate(intervals):
            if newInterval[1] < cur_sta:
                res.append(newInterval)
                return res + intervals[i:]
            elif cur_end < newInterval[0]:
                res.append([cur_sta, cur_end])
            else:
                newInterval = [min(newInterval[0], cur_sta), max(newInterval[1], cur_end)]
        res.append(newInterval)
        return res
