class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_l, row_h = 0, len(matrix) - 1
        while (row_l <= row_h):
            row_idx = (row_l + row_h) // 2
            sel_row = matrix[row_idx]
            
            # binary search within row
            col_l, col_r = 0, len(matrix[0]) - 1
            while (col_l <= col_r):
                col_idx = (col_l + col_r) // 2
                if (sel_row[col_idx] == target):
                    return True
                elif (sel_row[col_idx] > target):
                    col_r = col_idx - 1
                else:
                    col_l = col_idx + 1
            
            # update row idx
            if (col_l == 0):
                row_h = row_idx - 1
            elif (col_r == len(matrix[0]) - 1):
                row_l = row_idx + 1
            else:
                return False
        return False