class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        buttons = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        def recurce(digits):
            if len(digits) == 1: return [i for i in buttons[int(digits)]]
            else:
                l1 = [i for i in buttons[int(digits[0])]]
                l2 = recurce(digits[1:])
            return [a+b for a in l1 for b in l2]
        return recurce(digits)
        
"""
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
"""
