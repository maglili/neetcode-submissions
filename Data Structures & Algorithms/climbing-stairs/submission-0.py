class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[0] = 0
        # dp[0] = 0
        # dp[n] = num of ways to climb to n level
        dp = [0 * n + 1]
        dp[1] = 1
        dp[2] = 2