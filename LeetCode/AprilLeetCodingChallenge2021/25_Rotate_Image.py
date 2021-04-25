class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)-1
        for i in range(len(matrix)):
            if i > len(matrix)//2 and len(matrix)%2 != 0:
                break
            if i == len(matrix)//2 and len(matrix)%2 == 0:
                break
            for j in range(len(matrix)//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[size-j][i]
                matrix[size-j][i] = matrix[size-i][size-j]
                matrix[size-i][size-j] = matrix[j][size-i]
                matrix[j][size-i] = tmp
