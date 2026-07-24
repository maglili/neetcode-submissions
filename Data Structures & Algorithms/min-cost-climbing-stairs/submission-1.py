class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # base case
        if len(cost) <= 2:
            return min(cost)
        
        # Recurrence
        # A[i] = min((A[i-1] + cost[i-1], A[i-2]+ cost[i-2])
        n =  len(cost)
        one = 0
        two = 0

        for i in range(2, n+1):
            cur = min(one + cost[i-1], two + cost[i-2])
            two = one
            one = cur

        return one