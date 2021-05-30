class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
       if not s:
            return False
        a = (s + s)[1:-1]
        return a.find(s) != -1
"""      
        i = 2
        a = len(s)//2
        while a > 0:
            sub = s[0:a]
            if sub*i == s:
                return True
            i+=1
            a = len(s)//i
        return False
"""
