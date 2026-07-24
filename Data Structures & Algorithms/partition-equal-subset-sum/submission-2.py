class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False  

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for n in nums:
            next_dp = set()
            for t in dp:
                if t+n == target:
                    return True
                next_dp.add(t)
                next_dp.add(t+n)
            dp = next_dp

        return True if target in dp else False
