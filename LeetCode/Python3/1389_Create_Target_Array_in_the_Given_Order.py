class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, j in zip(nums, index):
            ans.insert(j, i)
        return ans
