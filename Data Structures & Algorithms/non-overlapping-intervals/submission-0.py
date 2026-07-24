class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        res = []
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])

        for sta, end in intervals[1:]:
            prev_sta, prev_end = res[-1]
            if sta < prev_end:
                cnt += 1
                res[-1] = (max(sta, prev_sta), min(end, prev_end))
            else:
                res.append((sta, end))
        print(res)

        return cnt
