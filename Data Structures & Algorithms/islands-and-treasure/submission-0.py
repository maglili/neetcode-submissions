class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        seem = set()

        # search the treasure chest.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    seem.add((r, c))

        def add_node(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r, c) in seem:
                return
            q.append((r, c))
            seem.add((r, c))

        # walk from treasure chest.
        cnt = 0
        while q:
            # walk from all the treasure chest in the same time
            q_len = len(q)
            for i in range(q_len):
                r, c = q.popleft()
                grid[r][c] = cnt

                add_node(r + 1, c)
                add_node(r - 1, c)
                add_node(r, c + 1)
                add_node(r, c - 1)
            cnt += 1
