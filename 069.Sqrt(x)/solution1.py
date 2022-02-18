"""
二分法
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = 1 << 16
        while l < r - 1:
            mid = (l + r) // 2
            if mid * mid < x:
                l = mid
            elif mid * mid > x:
                r = mid
            else:
                return mid

        return l


sol = Solution()
x = 1025
print(sol.mySqrt(x))