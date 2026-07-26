class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False

        target = sum(nums) / 2

        dp = set([])
        for num in nums:
            dp.add(num)
            dp2 = set([])
            for t in dp:
                if t == target:
                    return True
                dp2.add(t)
                dp2.add(t+num)
            dp = dp2

        return False
