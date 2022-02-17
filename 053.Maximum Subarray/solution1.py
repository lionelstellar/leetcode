"""
动态转移方程：dp[i] = max(dp[i] + nums[i - 1], nums[i - 1])
"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        maxSum = dp[0] = -10000
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
            maxSum = max(maxSum, dp[i])

        return maxSum



sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2]
print(sol.maxSubArray(nums))