class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        self.button = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        ans = []
        self.rec(ans,[],0,digits)
        return ans
    def rec(self, ans, subset, index, digits):
        if len(digits) == index:
            ans.append(''.join(subset))
            return
        for i in self.button[digits[index]]:
            subset.append(i)
            self.rec(ans, subset, index+1, digits)
            subset.pop()
