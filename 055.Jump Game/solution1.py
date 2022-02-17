"""
贪心：o(N), 0(1)
遍历数组，每一个点都计算当前能跳得最远的位置，不断刷新前i个位置能跳到的最远位置maxPos，直到maxPos >= n-1
如果遍历过程中i超过了maxPos，则说明前i-1个元素无法跳到i，返回False
"""
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        maxPos = 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, nums[i] + i)
                if maxPos >= n - 1:
                    return True

        return False

sol = Solution()
nums = [2,1,0,0,4]
print(sol.canJump(nums))