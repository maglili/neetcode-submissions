class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        area = 0
        temp_area = 0
        while (r < len(height)):
            h_l = height[l]
            h_r = height[r]
            if (h_r < h_l):
                diff = (h_l - h_r)
                temp_area += diff
                print("L:%d, R:%d, Diff:%d" %(l, r, diff))
            else: # h_r >= h_l
                area += temp_area
                temp_area = 0
                l = r
            r+=1
        return area
