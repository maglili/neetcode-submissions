class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        # 1. find a rotten fruit, and all fresh fruit num
        f_num = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    f_num += 1
        if f_num == 0:
            return 0

        # 2. Walk from all rotten fruit
        timestep = 0
        while q:
            for i in range(len(q)):
                cur_r, cur_c = q.popleft()
                for d_r, d_c in DIR:
                    new_r, new_c = cur_r + d_r, cur_c + d_c
                    if (0 <= new_r < ROWS) and (0 <= new_c < COLS) and (grid[new_r][new_c] == 1):
                        grid[new_r][new_c] = 2
                        f_num -= 1
                        q.append((new_r, new_c))
            if q:
                timestep += 1

        return timestep if f_num == 0 else -1
