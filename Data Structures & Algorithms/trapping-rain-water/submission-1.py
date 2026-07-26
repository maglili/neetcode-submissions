class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        area = 0
        while (r < len(height)):   
            h_r = height[r]
            h_l = height[l]

            if (h_r >= h_l):
                # calc area
                for i in range(l, r):
                    area += (min(h_l, h_r) - height[i])
                l = r
            r += 1
        return area
