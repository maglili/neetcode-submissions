class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0] # why no 0? in case negative num in nums
        cur_sum = 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            maxsub = max(cur_sum, cur_sum)
        return maxsub