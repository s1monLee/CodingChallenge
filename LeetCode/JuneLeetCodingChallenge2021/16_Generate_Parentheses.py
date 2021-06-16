class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        tmp = self.generateParenthesis(n-1)
        ans = set()
        for x in tmp:
            for i in range(len(x)):
                ans.add(x[:i]+'()'+x[i:])
        return list(ans)
