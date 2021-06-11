class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = cnt = 0
        for i in s:
            cnt += 1 if i == 'L' else -1
            if cnt == 0:
                ans+=1
        return ans
