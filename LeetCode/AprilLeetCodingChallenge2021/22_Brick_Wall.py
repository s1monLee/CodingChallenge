class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ans = collections.defaultdict(int)
        for row in wall:
            s = 0
            for i in row:
                s += i
                ans[s] += 1
            ans[s] = 0
        return len(wall) - max(ans.values())
