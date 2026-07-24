class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            h1 = heights[l]
            h2 = heights[r]
            area = (r - l) * min(h1, h2)
            res = max(res, area)
            if h1 < h2:
                l = l + 1
            else:
                r = r - 1
        return res
