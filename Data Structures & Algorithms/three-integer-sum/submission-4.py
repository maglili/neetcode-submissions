class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # for handle the dumplicate
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif val > 0:
                    r -= 1
                else:
                    l += 1
        return res
