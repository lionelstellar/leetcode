"""
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[1] * n for _ in range(m)]

        row0_obstacle_flag = False
        col0_obstacle_flag = False
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                    if i == 0:
                        row0_obstacle_flag = True
                    if j == 0:
                        col0_obstacle_flag = True
                elif i == 0:
                    if row0_obstacle_flag:
                        res[i][j] = 0
                elif j == 0:
                    if col0_obstacle_flag:
                        res[i][j] = 0
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[m - 1][n - 1]




sol = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(sol.uniquePathsWithObstacles(obstacleGrid))