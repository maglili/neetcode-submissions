class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        n =  len(cost)
        A = [0] * (n + 1)
        A[0] = 0
        A[1] = 0

        for i in range(2, n+1):
            A[i] = min(A[i-1] + cost[i-1], A[i-2]+ cost[i-2])

        print(A)
        return A[n]