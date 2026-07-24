class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seem = set([])

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def bfs(row, col):
            fifo = collections.deque()
            direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            fifo.append((row, col))
            seem.add((row, col))

            while fifo:
                r, c = fifo.popleft()
                for dir_r, dir_c in direction:
                    nr = r + dir_r
                    nc = c + dir_c
                    if (0<= nr < rows)\
                    and (0<= nc < cols)\
                    and grid[nr][nc] == "1"\
                    and (nr,nc) not in seem:
                        seem.add((nr, nc))
                        fifo.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seem:
                    bfs(r, c)
                    count += 1

        
        return count
                