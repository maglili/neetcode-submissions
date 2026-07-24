class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        n = len(nums)

        # A[i][j] = use nums[:i+1] can arrived target or not
        # row = val
        # col = item idx
        A = [[False] * (n + 1) for _ in range(target+1)]
        for j in range(n+1):
            A[0][j] = True

        for i in range(target+1): # amount: like backpack volume
            for j in range(1, n+1):
                num = nums[j-1]
                if num > i:
                    A[i][j] = A[i][j-1]
                else:
                    A[i][j] = A[i][j-1] or A[i-num][j-1]

        return A[target][n]