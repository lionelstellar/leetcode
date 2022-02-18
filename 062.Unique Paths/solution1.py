"""
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[m - 1][n - 1]




sol = Solution()
m = 3
n = 7
print(sol.uniquePaths(m, n))