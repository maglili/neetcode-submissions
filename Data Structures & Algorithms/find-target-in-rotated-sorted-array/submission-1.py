class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            print(m, nums[m])

            if nums[m] == target:
                return m
            elif nums[m] > target: # find smaller
                if nums[m] > nums[l] and nums[l] > nums[r]:
                    l = m + 1
                elif nums[m] > nums[l] and nums[l] < nums[r]:
                    r = m - 1
                elif nums[l] > nums[m] and nums[l] > nums[r]:
                    l = m + 1
                else: #nums[l] > nums[m] and nums[l] < nums[r]
                    return -1
            else: # find bigger
                if nums[m] > nums[l] and nums[l] > nums[r]:
                    r = m - 1
                elif nums[m] > nums[l] and nums[l] < nums[r]:
                    l = m + 1
                elif nums[l] > nums[m] and nums[l] > nums[r]:
                    r = m - 1
                else: #nums[l] > nums[m] and nums[l] < nums[r]:
                    return -1
        return -1

            
            