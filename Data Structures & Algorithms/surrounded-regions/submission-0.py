class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        seen1 = set()
        seen2 = set()
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # check if region is surround
        def is_sur(r, c, seen):
            seen.add((r, c))

            if (r == 0) or (r == ROWS - 1) or (c == 0) or (c == COLS - 1):
                return 0

            res = 1
            for d_r, d_c in DIR:
                next_r, next_c = r + d_r, c + d_c
                if (
                    (0 < next_r < ROWS)
                    and (0 < next_c < COLS)
                    and board[next_r][next_c] == "O"
                    and (next_r, next_c) not in seen
                ):
                    res &= is_sur(next_r, next_c, seen)
            return res

        # ark region to X
        def mark(r, c, seen):
            seen.add((r, c))
            board[r][c] = "X"

            for d_r, d_c in DIR:
                next_r, next_c = r + d_r, c + d_c
                if (
                    (0 < next_r < ROWS)
                    and (0 < next_c < COLS)
                    and board[next_r][next_c] == "O"
                    and (next_r, next_c) not in seen
                ):
                    return mark(next_r, next_c, seen)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in seen1:
                    if is_sur(r, c, seen1):
                        print("HI")
                        mark(r, c, seen2)
