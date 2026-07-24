class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # pairs: index, height
        res = 0
        for i, h in enumerate(heights):
            idx = i
            while stack and stack[-1][1] > h:
                prev_i, prev_h = stack.pop()
                res = max(res, prev_h * (i - prev_i))
                idx = prev_i
            stack.append((idx, h))

        for i, h in stack:
            res = max(res, h * (len(heights) - i))

        return res
