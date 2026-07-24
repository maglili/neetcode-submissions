class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        A = [0] * n
        A[0] = nums[0]
        A[1] = max(nums[0], nums[1])

        for i in range(2, n):
            A[i] = max(A[i-1], A[i-2]+nums[i])

        return A[n-1]

        