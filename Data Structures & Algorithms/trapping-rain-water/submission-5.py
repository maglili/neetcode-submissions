class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        l_max, r_max = height[0], height[r]
        
        res=0
        for n in height:
            if l_max < r_max:
                l_max = max(l_max, n)
                res += (l_max - n)
                l+= 1
            else:
                r_max = max(r_max, n)
                res += (r_max - n)
                r -= 1
        return res