"""

"""
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def zero_col(j):
            for k in range(m):
                matrix[k][j] = 0

        def zero_row(i):
            for k in range(n):
                matrix[i][k] = 0


        row = []
        col = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        for k in row:
            zero_row(k)
        for k in col:
            zero_col(k)


        print(matrix)
        return matrix



sol = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(sol.setZeroes(matrix))