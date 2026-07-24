from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # greedy + dp
        dp = []

        for v in nums:
            idx = bisect_left(dp, v)

            # 開新堆
            if idx == len(dp):
                dp.append(v)
            else:
                dp[idx] = v
        
        return len(dp)