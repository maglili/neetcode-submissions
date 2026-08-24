class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}  # (r, c): LIP
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(r, c, prev):
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS) or matrix[r][c] <= prev:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            res = 0
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = res
            return res

        max_res = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_res = max(max_res, dfs(r, c, -1))
        return max_res
