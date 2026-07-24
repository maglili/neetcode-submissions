class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = 0
        result |= self.chk_col(board)
        result |= self.chk_row(board)
        result |= self.chk_square(board)
        return (result == 0)
    
    def chk_square(self, board):
        tbl_list = [set() for _ in range(9)]
        for col in range(9):
            for row in range(9):
                square_idx = int(col / 3) * 3 + int(row / 3)
                num = board[col][row]
                if num == '.':
                    continue
                if num not in tbl_list[square_idx]:
                    tbl_list[square_idx].add(num)
                else:
                    return 1
        return 0

    def chk_col(self, board):
        for col in range(len(board)):
            tbl = set()
            for row in range(len(board)):
                num = board[row][col]
                if num == '.':
                    continue
                if num not in tbl:
                    tbl.add(num)
                else:
                    return 1
        return 0

    def chk_row(self, board):
        for row in board:
            tbl = set()
            for num in row:
                if num == '.':
                    continue
                if num not in tbl:
                    tbl.add(num)
                else:
                    return 1
        return 0