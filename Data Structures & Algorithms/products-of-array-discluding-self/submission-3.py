class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i, num in enumerate(nums):
            for j in range(n):
                if i == j:
                    continue
                res[j] *= num
        return res
