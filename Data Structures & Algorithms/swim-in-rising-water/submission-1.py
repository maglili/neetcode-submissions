class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        seen = set()
        minheap = [(grid[0][0], 0, 0)]  # cost, row, col
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])

        seen.add((0, 0))
        while len(minheap) > 0:
            t, r, c = heapq.heappop(minheap)
            if r == (ROWS - 1) and c == (COLS - 1):
                return t

            for dir_r, dir_c in DIR:
                new_r, new_c = r + dir_r, c + dir_c
                if (
                    new_r >= ROWS
                    or new_r < 0
                    or new_c >= COLS
                    or new_c < 0
                    or (new_r, new_c) in seen
                ):
                    continue
                heapq.heappush(minheap, (max(t, grid[new_r][new_c]), new_r, new_c))
                seen.add((new_r, new_c))
