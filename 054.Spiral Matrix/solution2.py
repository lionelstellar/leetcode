"""
用zip构造矩阵旋转的效果，每次削头即可
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            res += (matrix.pop(0))
            print(zip(*matrix))
            matrix = list(zip(*matrix))[::-1]

        return res

sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(*matrix)
print(list(zip(*matrix))[::-1])
# matrix = [[1]]
# matrix = [[]]
print(sol.spiralOrder(matrix))