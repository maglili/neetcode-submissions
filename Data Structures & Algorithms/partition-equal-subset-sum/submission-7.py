class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        n = len(nums)

        # A[i] = can arrived target j or not
        A = [False] * (target+1)
        A[0] = True

        for num in nums:
            for j in range(target, -1, -1): # amount: like backpack volume
                A[j] = A[j] or A[j-num]

        return A[target]