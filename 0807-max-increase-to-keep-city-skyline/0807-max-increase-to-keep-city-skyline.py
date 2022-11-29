class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                columns = list(zip(*grid))
                output += min(max(columns[j]), max(grid[i])) - grid[i][j]
        return output
                
        