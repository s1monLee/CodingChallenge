class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ''
        let, num = s[::2], s[1::2]
        for i, j in zip(let, num):
            ans+=i + chr(ord(i)+int(j))
        if len(let)>len(num):
            ans+=let[-1]
        return ans
