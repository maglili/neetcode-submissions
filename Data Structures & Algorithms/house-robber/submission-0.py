class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        A = [0] * (n + 1)
        A[0] = 0
        A[1] = nums[0]
        A[2] = max(nums[0], nums[1])

        for i in range(3, n+1):
            A[i] = max(A[i-1], A[i-2]+nums[i-1])

        return A[n]

        