class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        self.mem = [[-1]*len(grid[0]) for i in range(len(grid))]
        def dfs(grid, row: int, col: int) -> int:
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 1:
                return 0
            if row == len(grid)-1 and col == len(grid[0])-1:
                return 1
            if self.mem[row][col] > -1:
                return self.mem[row][col]
            self.mem[row][col] = dfs(grid, row, col+1) + dfs(grid, row+1, col)
            return self.mem[row][col]
        
        return dfs(grid, 0, 0)
        
