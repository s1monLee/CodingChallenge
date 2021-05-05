class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        jmp = 1
        while r < len(nums)-1:
            jmp += 1
            tmp = max(i+nums[i] for i in range(l, r+1))
            l, r = r, tmp
        return jmp
