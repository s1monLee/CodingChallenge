class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                cnt += 1
                if i - 2 < 0 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
            if cnt > 1: break
                
        return cnt<=1
