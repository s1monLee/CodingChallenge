class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        
        for r in range(2, numRows+1):
            tmp = [1]
            for c in range(1, r-1):
                tmp.append(ans[-1][c] + ans[-1][c-1])
            tmp.append(1)    
            ans.append(tmp)
        return ans
