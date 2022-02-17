"""

"""
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        board = [[0] * n for _ in range(n)]
        num = 1
        length = n
        while length > 1:
            x = y = (n - length) // 2
            for _ in range(length - 1):
                board[x][y] = num
                num += 1
                y += 1
            for _ in range(length - 1):
                board[x][y] = num
                num += 1
                x += 1
            for _ in range(length - 1):
                board[x][y] = num
                num += 1
                y -= 1
            for _ in range(length - 1):
                board[x][y] = num
                num += 1
                x -= 1
            length -= 2

        if n % 2 == 1:
            board[(n - 1)//2][(n - 1)//2] = n * n

        return board


sol = Solution()
n = 2
print(sol.generateMatrix(n))