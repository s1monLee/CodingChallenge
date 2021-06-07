class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp0 = cost[0]
        dp1 = cost[1]
        for i in range(2, len(cost)):
            tmp = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = tmp
        return min(dp0, dp1)
    """
    class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])
    """
