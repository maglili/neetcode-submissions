class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[0] = 0
        # dp[1] = 1 (only 1)
        # dp[2] = 2 (1+1 or 2)
        # dp[n] = num of ways to climb to n level
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]