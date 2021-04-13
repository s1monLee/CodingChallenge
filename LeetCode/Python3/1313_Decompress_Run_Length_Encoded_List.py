class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            if i%2 == 0: ans += [nums[i+1]]*num
        return ans
