"""
直接推导出旋转公式：
matrix[raw][col] = matrix[n - 1 - col][raw]
"""
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        import math
        for i in range(math.floor(n / 2)):
            for j in range(math.ceil(n / 2)):
                matrix[i][j] , matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i] = \
                    matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i], matrix[i][j]

        return matrix

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(sol.rotate(matrix))