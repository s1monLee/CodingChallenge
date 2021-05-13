class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col, row = len(matrix), len(matrix[0])
        self.arr = [[0 for _ in range(row)] for _ in range(col)]
        for i in range(col):
            s = 0
            for j in range(row):
                s += matrix[i][j]
                self.arr[i][j] += s
                if i > 0:
                    self.arr[i][j] += self.arr[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.arr[row2][col2]
        bottom_left  = self.arr[row2][col1-1] if col1 >= 1 else 0
        top_right    = self.arr[row1-1][col2]  if row1 >= 1 else 0
        top_left     = self.arr[row1-1][col1-1] if col1 >= 1 and row1 >= 1 else 0
        return bottom_right - bottom_left - top_right + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
