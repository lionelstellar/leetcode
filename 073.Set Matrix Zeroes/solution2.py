"""
O(1)空间复杂度，用2个flag表示0行和0列是否需要置0，然后把需要置零的行或列头部标0作为置零的判断条件，最后先把子矩阵zeroes，
再把0行与0列按flag判断是否需要zeroes
"""
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_col_flag = zero_row_flag = False
        for i in range(m):
            if matrix[i][0] == 0:
                zero_col_flag = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                zero_row_flag = True
                break

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0


        for i in range(1, m):
            if not matrix[i][0]:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if not matrix[0][j]:
                for i in range(1, m):
                    matrix[i][j] = 0

        if zero_col_flag:
            for i in range(m):
                matrix[i][0] = 0
        if zero_row_flag:
            for j in range(n):
                matrix[0][j] = 0

        return matrix



sol = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
print(sol.setZeroes(matrix))