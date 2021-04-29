class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findIndex(nums, target, start = True):
            index = -1
            left, right = 0, len(nums)-1
            
            while left <= right:
                mid = left + (right - left)//2
                
                if(nums[mid] == target):
                    index = mid
                    if start:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return index
        
        ans = [-1,-1]
        ans[0] = findIndex(nums, target, True)
        ans[1] = findIndex(nums, target, False)
        
        return ans
