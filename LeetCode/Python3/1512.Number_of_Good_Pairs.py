"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = 0
        for i, n in enumerate(nums):
            for j in range(i+1,len(nums)):
                if n == nums[j]:
                    pair+=1
        return pair
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num = 0
        pair = {}
        for i in nums:
            if i in pair:
                num += pair[i]
                pair[i] += 1 
            else:
                pair[i] = 1
        return num
