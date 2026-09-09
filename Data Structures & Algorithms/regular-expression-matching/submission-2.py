class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = {}  # memo

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j == n:
                dp[(i, j)] = i == m
                return dp[(i, j)]

            match = i < m and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < n and p[j + 1] == "*":
                dp[(i, j)] = (
                    dfs(i, j + 2)  # not use *
                    or (match and dfs(i + 1, j))  # use *
                )
                return dp[(i, j)]

            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return dp[(i, j)]

        return dfs(0, 0)
