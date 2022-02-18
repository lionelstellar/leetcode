"""
"""
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = [[0] * n for _ in range(m)]
        res[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    res[i][j] = res[i][j - 1] + grid[i][j]
                elif j == 0 and i > 0:
                    res[i][j] = res[i - 1][j] + grid[i][j]
                elif j > 0 and i > 0:
                    res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]

        return res[m - 1][n - 1]

sol = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
print(sol.minPathSum(grid))