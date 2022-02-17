"""
仿照sudoku solver,超时了
"""

import copy
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        def dfs(cnt, board):
            if cnt == 0:
                res.append(board)
                return board

            for i in range(n):
                for j in range(n):
                    if raw[i] == col[j] == sum[i + j] == diff[i - j] == False:
                        raw[i] = col[j] = sum[i + j] = diff[i - j] = True
                        new_board = copy.deepcopy(board)
                        new_board[i][j] = "Q"
                        dfs(cnt - 1, new_board)
                        raw[i] = col[j] = sum[i + j] = diff[i - j] = False


        board = [["."] * n for _ in range(n)]

        raw = [False] * n
        col = [False] * n
        sum = {}
        for i in range(2 * n):
            sum[i] = False
        diff = {}
        for i in range(1 - n, n):
            diff[i] = False

        res = []
        dfs(n, board)

        new_res = []
        for solution in res:
            new_solution = []
            for elem in solution:
                new_solution.append("".join(elem))
            if new_solution not in new_res:
                new_res.append(new_solution)

        return new_res



sol = Solution()
n = 4
print(sol.solveNQueens(n))