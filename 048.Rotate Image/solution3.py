"""
python的zip函数自带旋转效果
"""
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = list(zip(*matrix[::-1]))
        return matrix

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(sol.rotate(matrix))