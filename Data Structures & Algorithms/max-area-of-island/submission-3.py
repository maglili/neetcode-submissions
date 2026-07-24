class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        res = 0
        seen = set([])

        DIRECT = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # up, down, left, right

        def bfs(row, col) -> int:
            q = collections.deque()
            seen.add((row, col))
            q.append((row, col))
            area = 0

            while q:
                r, c = q.popleft()
                area += 1
                for d_r, d_c in DIRECT:
                    new_r, new_c = r + d_r, c + d_c
                    if (
                        (0 <= new_r < rows)
                        and (0 <= new_c < cols)
                        and (grid[new_r][new_c] == 1)
                        and ((new_r, new_c) not in seen)
                    ):
                        seen.add((new_r, new_c))
                        q.append((new_r, new_c))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = bfs(r, c)
                    if area > res:
                        res = area
        return res
