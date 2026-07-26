class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = 0
        result |= self.chk_col(board)
        result |= self.chk_row(board)
        result |= self.chk_square(board)
        return (result == 0)
    
    def chk_square(self, board):
        tbl_list = [{} for _ in range(int((len(board) / 3)**2))]
        for x in range(len(board)):
            for y in range(len(board)):
                square_idx = int(x / 3) * 3 + int(y / 3)
                num = board[x][y]
                if num == '.':
                    continue
                if num not in tbl_list[square_idx]:
                    tbl_list[square_idx][num] = True
                else:
                    print("square invalid:", num)
                    print("tbl:", tbl_list[square_idx][num])
                    return 1
        for tbl in tbl_list:
            if len(tbl) == 0:
                return 1
        return 0

    def chk_col(self, board):
        for x in range(len(board)):
            tbl = {}
            for y in range(len(board)):
                num = board[x][y]
                if num == '.':
                    continue
                if num not in tbl:
                    tbl[num] = True
                else:
                    print("col invalid:", num)
                    print("tbl:", tbl)
                    return 1
            if len(tbl) == 0:
                return 1
        return 0

    def chk_row(self, board):
        for row in board:
            tbl = {}
            for num in row:
                if num == '.':
                    continue
                if num not in tbl:
                    tbl[num] = True
                else:
                    print("row invalid:", num)
                    print("tbl:", tbl)
                    return 1
            if len(tbl) == 0:
                return 1
        return 0