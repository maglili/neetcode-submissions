class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # scan 0
        is_col_0_zero = False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if c == 0:
                        is_col_0_zero = True
                    else:
                        matrix[0][c] = 0
                    matrix[r][0] = 0

        # mark 0
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # mark first row
        if matrix[0][0] == 0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0

        # mark first col
        if is_col_0_zero:
            for r in range(len(matrix)):
                matrix[r][0] = 0
