class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BLOCK_SIZE = 3
        rows = len(board)
        cols = len(board[0])

        # check every row
        for r in range(rows):
            seem = set()
            for c in range(cols):
                if board[r][c].isdigit() and board[r][c] in seem:
                    return False
                seem.add(board[r][c])

        # check every row
        for c in range(cols):
            seem = set()
            for r in range(rows):
                if board[r][c].isdigit() and board[r][c] in seem:
                    return False
                seem.add(board[r][c])

        for s_r in range(0, rows, BLOCK_SIZE):
            for s_c in range(0, cols, BLOCK_SIZE):
                seem = set()
                for r in range(s_r, s_r + BLOCK_SIZE):
                    for c in range(s_c, s_c + BLOCK_SIZE):
                        if board[r][c].isdigit() and board[r][c] in seem:
                            return False
                        seem.add(board[r][c])
        return True