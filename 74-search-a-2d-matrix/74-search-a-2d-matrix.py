class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, 0
        i = 0
        while i < len(matrix):
            if matrix[i][0] > target:
                break
            row = i
            i += 1
        
        for i in matrix[row]:
            if i == target:
                return True
        
        return False
            