class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        # A[i][j] = use nums[:i+1] can arrived target or not
        # row = val
        # col = item idx
        # A[0][0] is True. 0 amout cost 0 item
        A = [[False] * (len(nums) + 1) for _ in range(target+1)]
        for row in  range(target+1):
            A[row][0] = True

        for i in range(target+1): # amount: like backpack volume
            for j in range(1, len(nums)):
                if j > i:
                    A[i][j] = A[i][j-1]
                else:
                    A[i][j] = A[i][j-1] or A[i][j-2]

        return A[i][j]