class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        gold = sum(range(len(nums)+1))
        res = 0
        for n in nums:
            res += n
        return gold - res