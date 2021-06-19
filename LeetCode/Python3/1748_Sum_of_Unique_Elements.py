class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mem = [0]*101
        ans = cnt = 0
        for i in nums:
            mem[i]+=1
        while cnt < 101:
            if mem[cnt] == 1:
                ans += cnt
            cnt += 1
        return ans
                
