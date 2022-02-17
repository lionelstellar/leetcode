"""
动态转移方程：dp[i] = max(dp[i] + nums[i - 1], nums[i - 1])
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        def valid(i, j, direction):
            nonlocal res
            new_row, new_col = i + direction_dict[direction][0], j + direction_dict[direction][1]

            if 0 <= new_row < row and 0 <= new_col < col and matrix[new_row][new_col] != pickup:
                res.append(matrix[new_row][new_col])
                matrix[new_row][new_col] = pickup
                return new_row, new_col, direction
            else:
                return valid(i, j, next_direct[direction])




        direction_dict = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        next_direct = {"up": "right", "down": "left", "left": "up", "right": "down"}
        row, col = len(matrix), len(matrix[0])

        res = []
        pickup = 200
        i = 0
        j = -1
        direction = "right"
        for _ in range(row * col):
            i, j, direction = valid(i, j, direction)

        return res

sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1]]
matrix = [[]]
print(sol.spiralOrder(matrix))