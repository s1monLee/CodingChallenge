class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cur = ans = 0
        j = 0
        mem = set()
        for i in range(len(nums)):
            while nums[i] in mem:
                cur -= nums[j]
                mem.remove(nums[j])
                j+=1
            mem.add(nums[i])
            cur+=nums[i]
            ans = max(cur, ans)
            
        return ans
