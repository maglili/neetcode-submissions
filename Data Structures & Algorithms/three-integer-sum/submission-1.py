class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # for handle the dumplicate
        res = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                while l > 0 and nums[l] == nums[l - 1]:
                    l += 1
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    res.append([nums[i], nums[l], nums[r]])
                elif val > 0:
                    r -= 1
                else:
                    l += 1
        return res
