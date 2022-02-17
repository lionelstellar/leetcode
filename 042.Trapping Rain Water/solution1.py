"""
dp保存2个数组，分别是左侧最高和右侧最高
"""
class Solution:
    def trap(self, height: list[int]) -> int:
        leftmax =  [0] * len(height)
        rightmax =  [0] * len(height)
        leftmax[0] = height[0]
        rightmax[-1] = height[-1]
        sum = 0

        for i in range(1,len(height)):
            leftmax[i] = max(leftmax[i - 1], height[i])

        for j in range(len(height) - 2, 0, -1):
            rightmax[j] = max(rightmax[j + 1], height[j])

        for i in range(1, len(height) - 1):
            sum += min(leftmax[i], rightmax[i]) - height[i]

        return sum



sol = Solution()
height = [4,2,0,3,2,5]
print(sol.trap(height))