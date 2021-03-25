class Solution:
    def dfs(self, i,j, grid):
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == 1:
            ans = 1
            grid[i][j] = 0
            for r,c in [[-1,0], [1,0], [0,1], [0,-1]]:
                    ans+=self.dfs(i+r, j+c, grid)
            return ans
        else:
            return 0
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                    result = max(self.dfs(i,j, grid),result)
        return result
        