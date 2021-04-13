class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []: return 0
        lenght = 0
        for i in range(1,len(nums)):
            if nums[lenght] < nums[i]:
                lenght += 1
                nums[lenght] = nums[i]
        return lenght+1
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []: return 0
        last = nums[0]
        ind = []
        ans = 1
        for i in range(1, len(nums)):
            if(nums[i] == last):
                ind.append(i)
            else:
                ans += 1
                last = nums[i]
        ind = ind[::-1]
        for i in range(len(ind)):
            nums.pop(ind[i])
            
        return ans
"""
