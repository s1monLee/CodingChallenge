class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        out = 0
        
        for n in nums:
            if n-1 not in nums:
                tmp = n
                while tmp in nums:
                    tmp+=1
                out = max(out, tmp-n)
        return out
