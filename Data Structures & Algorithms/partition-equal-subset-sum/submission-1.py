class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if len(nums) % 2 != 0:
            return False      

        dp = set()
        dp.add(nums[0])
        for num in nums[1:]:
            dp2 = set()
            for t in dp:
                if t == target:
                    return True
                dp2.add(t)
                dp2.add(t+num)
            dp = dp2

        return True if target in dp else False
