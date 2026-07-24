class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 1. 反向思考，從邊緣開始可以走到的點就是能走到海裡，所以走邊緣往裡面走
        # 2. 把 PAC 跟 ATL 都做一次，交集就是可以走到兩邊的位置
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, seen_set, prev_hight):
            if (
                (r < 0)
                or (c < 0)
                or (r == ROWS)
                or (c == COLS)
                or ((r, c) in seen_set)
                or (heights[r][c] < prev_hight)
            ):
                return
            seen_set.add((r, c))

            dfs(r + 1, c, seen_set, heights[r][c])
            dfs(r - 1, c, seen_set, heights[r][c])
            dfs(r, c + 1, seen_set, heights[r][c])
            dfs(r, c - 1, seen_set, heights[r][c])

        # 從上下開始
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # 左右開始走
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # loop 所有的 node，找出現在兩個 set 的點
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        return res
