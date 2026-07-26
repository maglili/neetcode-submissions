class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        seen = set([])

        def dfs(row, col, i):
            if i == len(word):
                return True

            if (i > len(word)
                or row > rows 
                or row < 0
                or col > cols
                or col < 0 
                or board[row][col] != word[i]
                or (row, col) in seen):
                return False

            seen.add((row, col))

            return (dfs(row+1, col, i+1)
                or dfs(row-1, col, i+1)
                or dfs(row, col+1, i+1)
                or dfs(row, col-1, i+1)
                )

            seen.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False
