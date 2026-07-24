class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:      
        n =  len(cost)
        one = 0
        two = 0

        for i in range(2, n+1):
            cur = min(one + cost[i-1], two + cost[i-2])
            two = one
            one = cur

        return one