class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            maxjump = 0
            for i in range(l, r + 1):
                maxjump = max(maxjump, nums[i])
            res += 1
            l = r + 1
            r = r + maxjump

        return res
