class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while(l < r):
            area = self.calc_area(heights[l], heights[r], r-l)
            if area > max_area:
                max_area = area
            if l <= r:
                l += 1
            else:
                r -= 1
        return max_area

    def calc_area(self, height1, height2, distance):
        return min(height1, height2) * distance
        