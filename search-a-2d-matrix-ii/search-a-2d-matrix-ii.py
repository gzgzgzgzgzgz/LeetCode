class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        row, column = 0, len(matrix[0]) - 1
        while row < len(matrix) and column >= 0:
            val = matrix[row][column]
            if val == target:
                return True
            elif val < target:
                row+=1
            else:
                column-=1
        return False
        