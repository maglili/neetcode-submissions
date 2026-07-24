class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        area = 0
        temp_max_h = 0
        while (r < len(height)):   
            
            h_l = height[l]

            # get max r
            for i in range(r, len(height)):
                h_temp = height[i]
                if h_temp >= h_l:
                    r = i
                    break
                else:
                    if h_temp >temp_max_h:
                        temp_max_h = h_temp
                        r = i
            h_r = height[r]

            # calc addr
            for i in range(l+1, r):
                area += (min(h_l, h_r) - height[i])
            print(l,r, area)

            l = r
            r += 1
            temp_max_h = 0
        return area
