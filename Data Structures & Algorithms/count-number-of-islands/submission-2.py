class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0

        # 上、下、左、右 四個探險方向的常數定義
        DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def bfs(start_row: int, start_col: int):
            queue = collections.deque()

            # 1. 起點進 Queue，立刻標記已造訪
            queue.append((start_row, start_col))
            visited.add((start_row, start_col))

            while queue:
                curr_row, curr_col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    next_row = curr_row + dr
                    next_col = curr_col + dc

                    # 2. 完美的邊界與條件把關（加上空格，易讀性大暴增）
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == "1"
                        and (next_row, next_col) not in visited
                    ):
                        # 3. 鄰居進 Queue，立刻鎖死標記
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))

        # 主程式：地毯式搜索整張地圖
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island_count += 1

        return island_count
