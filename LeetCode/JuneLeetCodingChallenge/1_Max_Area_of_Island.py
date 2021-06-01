class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        self.area = 0
        self.g = grid
        def rec(i: int, j: int):
            
            if i<0 or j<0 or i>=len(self.g) or j >= len(self.g[0]) or self.g[i][j]!=1:
                return
            self.area +=1
            self.g[i][j] = 0
            rec(i+1, j)
            rec(i-1, j)
            rec(i, j+1)
            rec(i, j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    rec(i,j)
                    ans = max(self.area, ans)
                    self.area = 0
        return ans
