class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)+1):
            for sub in itertools.combinations(nums,i):
                xor = 0
                for i in sub:
                    xor^=i
                ans+=xor
        return ans
"""
        bits = 0
        for a in nums:
            bits |= a
        return bits * int(pow(2, len(nums)-1))
"""
        self.ans = 0
        def bfs(nums: List[int], pos: int, cur: int):
            if pos == len(nums):
                self.ans += cur
                return
            bfs(nums, pos+1, cur)
            bfs(nums, pos+1, cur^nums[pos])
        bfs(nums, 0, 0)
        return self.ans
"""
