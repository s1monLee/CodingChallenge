class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hor = sorted(horizontalCuts)
        ver = sorted(verticalCuts)
        hor = [0] + hor + [h]
        ver = [0] + ver + [w]
        a = b = 0
        for i in range(1, len(hor)):
            a = max(a, hor[i] - hor[i-1])
        for j in range(1, len(ver)):
            b = max(b, ver[j] - ver[j-1])
        return (a * b) % (10**9 + 7)
