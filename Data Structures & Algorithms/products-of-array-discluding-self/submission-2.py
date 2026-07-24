class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i, n in enumerate(nums):
            for j, m in enumerate(res):
                if i == j:
                    continue
                res[j] = m * n
        return res
