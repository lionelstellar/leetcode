"""
dp双数组的优化：双指针
"""
class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax = height[left]
        rightmax = height[right]
        sum = 0

        while left < right:
            if height[left] < height[right]:
                sum += leftmax - height[left]
                left += 1
                leftmax = max(leftmax, height[left])
            else:
                sum += rightmax - height[right]
                right -= 1
                rightmax = max(rightmax, height[right])
        return sum

sol = Solution()
height = [4,2,0,3,2,5]
print(sol.trap(height))