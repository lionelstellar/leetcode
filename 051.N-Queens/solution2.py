"""
在solution1的基础上做出改进，把结果直接保存为一个以为数组cols，(i,cols[i])表示棋盘的i行、cols[i]列上放皇后，把i从n-1到0进行DFS并回溯，
每生成一个合法排布就用gen_board(cols)来生成board，并append到结果中去
"""
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def gen_board(cols):
            result = []
            for elem in cols:
                tmp = ['.'] * n
                tmp[elem] = 'Q'
                result.append("".join(tmp))
            return result

        def dfs(row, cols):
            if row < 0:
                res.append(gen_board(cols))
                return

            for j in range(n):
                if j not in cols and row + j not in diag_sum and row - j not in diag_diff:
                    cols[row] = j
                    diag_sum.add(row + j)
                    diag_diff.add(row - j)
                    dfs(row - 1, cols)
                    cols[row] = -1
                    diag_sum.remove(row + j)
                    diag_diff.remove(row - j)

        cols = [-1] * n
        diag_sum = set()
        diag_diff = set()

        res = []
        dfs(n - 1, cols)

        return res



sol = Solution()
n = 6
print(sol.solveNQueens(n))