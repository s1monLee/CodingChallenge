class Solution:
    def findCenter(self, a: List[List[int]]) -> int:
        return a[0][0] if a[0][0] == a[1][0] or a[0][0]==a[1][1] else a[0][1]
