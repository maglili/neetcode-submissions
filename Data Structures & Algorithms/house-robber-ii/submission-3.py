class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        if len(nums) == 0:
            return 0
            
        if len(nums) == 1:
            return nums[0]
            
        # A[i] = max(A[i-1], A[i-2] + wi)
        A = [0] * len(nums)
        A[0] = nums[0]
        A[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            A[i] = max(A[i-1], A[i-2] + nums[i])

        return A[len(nums)-1]
