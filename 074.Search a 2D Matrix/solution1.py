"""
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        p, q = 0, 0
        r, s = m - 1, n - 1
        while p < r:
            mid = (p + r) // 2
            if matrix[mid][0] < target:
                p = mid
            elif matrix[mid][n - 1] > target:
                r = mid

        while


sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix, target))