class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # A[i] = 從位置 i 到尾的 subseque 長度 (nums[i:])
        # A[i] = max(A[i], 1 + A[j]) for all j > i where nums[i] < nums[j]
        A = [1] * len(nums)
        res = 0
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    A[i] = max(A[i], A[j]+1)
            if A[i] > res:
                res = A[i]
        return res