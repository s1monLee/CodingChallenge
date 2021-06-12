class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        ans = 0
        for i in range(N):
            ans += mat[i][i]
            ans += mat[N-i-1][i]
        return ans if N%2==0 else ans-mat[N//2][N//2]
