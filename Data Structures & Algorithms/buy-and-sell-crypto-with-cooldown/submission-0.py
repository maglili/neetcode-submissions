class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key = (day, state), val = max_profit
        # state
        # True: buy
        # False: sell

        def dfs(i, state):
            if i >= len(prices):
                return 0

            if (i, state) in dp:
                return dp[(i, state)]

            if state:
                buy = dfs(i + 1, not state) - prices[i]
                cooldown = dfs(i + 1, state)
                dp[(i, state)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not state) + prices[i]
                cooldown = dfs(i + 1, state)
                dp[(i, state)] = max(sell, cooldown)

            return dp[(i, state)]

        return dfs(0, True)
