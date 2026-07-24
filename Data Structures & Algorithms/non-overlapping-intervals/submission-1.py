class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]

        for sta, end in intervals[1:]:
            if sta < prev_end:
                cnt += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end

        return cnt
