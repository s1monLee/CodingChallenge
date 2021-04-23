class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = []
        a, b = 0, 0
        for i in s:
            if i == '1' and b == 0:
                a += 1
            elif i == '1' and b != 0:
                ans.append(b)
                b = 0
                a += 1
            if i == '0' and a == 0:
                b += 1
            elif i == '0' and a != 0:
                ans.append(a)
                a = 0
                b += 1
        if a != 0:
            ans.append(a)
        else:
            ans.append(b)
        n = 0
        for i in range(len(ans)-1):
            n += min(ans[i], ans[i+1])
        print(ans)  
        return n
