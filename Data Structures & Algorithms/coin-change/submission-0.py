class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cur = []
        min_len = float('inf')

        def dfs(cur_sum):
            nonlocal min_len
            if cur_sum == amount:
                if len(cur) < min_len:
                    min_len = len(cur)
            
            if cur_sum > amount:
                return

            for num in coins:
                cur.append(num)
                dfs(cur_sum+num)
                cur.pop()

        dfs(0)
        return min_len if min_len != float('inf') else -1