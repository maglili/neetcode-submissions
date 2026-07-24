class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # A[i] = min coin to arrived amount i
        # A[i] = min of A[i-c] + 1 for each possible coin
        A = [float('inf')]* (amount + 1)
        A[0] = 0 # amount 0 cost 0 coin

        for i in range(1, amount + 1):
            for c in coins:
                if i-c>=0:
                    A[i] = min(A[i], A[i-c] + 1)
        
        return A[amount] if A[amount] != float('inf') else -1
            
