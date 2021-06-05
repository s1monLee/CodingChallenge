class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = b = c = 0
        for i in firstWord:
            a+=ord(i)-ord('a')
            a*=10
        for i in secondWord:
            b+=ord(i)-ord('a')
            b*=10
        for i in targetWord:
            c+=ord(i)-ord('a')
            c*=10
        print(a,b,c)
        return a+b==c
