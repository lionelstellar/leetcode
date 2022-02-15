"""
求中心点，围绕其旋转
"""
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def new_point(origin, vec):
            return [int(origin[0] + vec[0]), int(origin[1] + vec[1])]

        n = len(matrix[0])

        if n % 2 == 0:
            loss = 0.5
            odd = 0
        else:
            loss = 0
            odd = 1

        center = (n / 2 - loss, n / 2 - loss)
        #print(center)
        i = j = 0

        while i <= n//2 - loss:
            if odd:j = 1
            else: j = 0
            while j <=  n//2 - loss:
                a1, b1 = new_point(center, (i+loss, j+loss))
                a2, b2 = new_point(center, (-j-loss, i+loss))
                a3, b3 = new_point(center, (-i-loss, -j-loss))
                a4, b4 = new_point(center, (j+loss, -i-loss))
                #print([a1,b1], [a2,b2], [a3,b3], [a4,b4], i, j)
                tmp = matrix[a1][b1]
                matrix[a1][b1] = matrix[a2][b2]
                matrix[a2][b2] = matrix[a3][b3]
                matrix[a3][b3] = matrix[a4][b4]
                matrix[a4][b4] = tmp
                j += 1
            i += 1

        return matrix



sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(sol.rotate(matrix))