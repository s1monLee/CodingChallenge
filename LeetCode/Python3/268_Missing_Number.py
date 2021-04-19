class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for i, n in enumerate(nums):
            xor = xor ^ i ^ n
        return xor
