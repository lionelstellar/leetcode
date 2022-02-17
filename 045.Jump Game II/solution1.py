"""
贪心：
遍历数组，每一个点都计算当前能跳得最远的位置，不断刷新前i个位置能跳到的最远位置maxPos
maxPos: 前i个能跳到的最原位置
end:    上一个跳到maxPos的起点
step:   上一个跳到maxPos所用步数
"""
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, nums[i] + i)
                if i == end:
                    end = maxPos
                    step += 1

        return step

sol = Solution()
nums = [2,3,1,1,4]
print(sol.jump(nums))