class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #一刀切下去，必定是一邊完全有序
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m

            # 如果左半邊是有序的
            if nums[l] <= nums[m]:
                # target 是否落在右半邊
                if target > nums[m] or target < nums[l]:
                    l = m + 1 # 往右找
                else:
                    r = m - 1 # 往左找
            
            # 如果右半邊是有序的
            else:
                # target 是否落在左半邊
                if target < nums[m] or target > nums[r]:
                    r = m - 1 # 往左找
                else:
                    l = m + 1 # 往右找
        return -1

            
            