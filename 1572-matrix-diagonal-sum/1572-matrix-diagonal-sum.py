class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        left_x = 0
        ln = len(mat[0])
        while left_x < ln:
            total += mat[left_x][left_x] + mat[left_x][ln - 1 - left_x]
            left_x += 1
        
        return total - mat[int((ln)/2)][int((ln)/2)] if ln%2 else total
            