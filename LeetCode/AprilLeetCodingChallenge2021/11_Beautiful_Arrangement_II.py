class Solution:
    def constructArray(self, n, k):
        ans = [i for i in range(1, n - k)]
        for d in range(k+1):
            if d % 2 == 0:
                ans.append(n-k + d//2)
            else:
                ans.append(n - d//2)
        return ans
