"""
N-皇后基础上稍加修改即可
"""
class Solution:
    def totalNQueens(self, n: int) -> int:

        def dfs(row, cols):
            nonlocal  ret
            if row < 0:
                ret += 1
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

        ret = 0
        dfs(n - 1, cols)
        return ret




sol = Solution()
for i in range(10):
    print(sol.totalNQueens(i))