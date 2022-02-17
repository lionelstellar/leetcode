"""

"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n

        ret = pow(x, n)
        return ret


sol = Solution()
x = 2.10000
n = 3

x = 2.00000
n = 10
print(sol.myPow(x,n))