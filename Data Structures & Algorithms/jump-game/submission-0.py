class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_frag = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= end_frag:
                end_frag = i
        return end_frag == 0
