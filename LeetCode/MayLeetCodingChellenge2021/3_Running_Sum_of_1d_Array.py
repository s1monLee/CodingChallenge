class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #solution 1

        #for i in range(1, len(nums)):
           # nums[i]+=nums[i-1]
        #return nums
        
        #solution 2
        #return accumulate(nums)
        
        #solution 3
        return [sum(nums[:i+1]) for i in range(len(nums))]
