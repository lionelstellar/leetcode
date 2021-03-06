"""
斐波拉切数列dp
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]

sol = Solution()
n = 5
print(sol.climbStairs(n))