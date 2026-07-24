class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # sort array by start val
        res = [intervals[0]]

        for sta, end in intervals[1:]:
            if sta <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([sta, end])
        return res
