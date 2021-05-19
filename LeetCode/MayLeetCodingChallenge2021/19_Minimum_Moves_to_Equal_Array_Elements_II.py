class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        m = int(median(nums))
        return sum(abs(i-m) for i in nums)
