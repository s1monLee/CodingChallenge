class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            if i%2 == 0: ans += [nums[i+1]]*num
        return ans
        #one-line
        #return sum([nums[i]*[nums[i+1]] for i in range(0,len(nums),2)],[])
