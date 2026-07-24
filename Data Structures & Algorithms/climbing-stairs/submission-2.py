class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[0] = 0
        # dp[1] = 1 (only 1)
        # dp[2] = 2 (1+1 or 2)
        # dp[n] = num of ways to climb to n level
        if n <= 2:
            return n

        one = 1 
        two = 2 # newer

        for i in range(3, n+1):
            cur = one + two
            one = two
            two = cur

        return two