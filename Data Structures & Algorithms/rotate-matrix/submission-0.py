class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # [1,2]
        # [3,4]

        # [1,3]
        # [2,4]

        # [3,1]
        # [4,2]

        # 1. traspose
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

        # 2. reverse
        for r in range(len(matrix)):
            matrix[r].reverse()
