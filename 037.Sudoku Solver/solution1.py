"""
DFS回溯法：
使用三个标记列表row, col, block
row[i][digit]==True表示第i行有(digit+1)这个数出现
col[digit][j]==True表示第j列有(digit+1)这个数出现
block[i//3][j//3][digit]==True表示第i行j列所在的sub-box有(digit+1)这个数出现

首先遍历数独表盘，spaces收集待填入数字格子的坐标(i,j),并将row,col,block初始化并更新

然后从spaces中的第一个元素开始dfs，直到最后一个位置填完数字，才打到valid状态

填数字：
row[i][digit] = col[digit][j] = block[i // 3][j // 3][digit] = True
board[i][j] = str(digit + 1)

回溯：
row[i][digit] = col[digit][j] = block[i // 3][j // 3][digit] = False


"""

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                # for i in range(9):
                #     print(board[i])
                return

            i, j = spaces[pos]
            for digit in range(9):
                if row[i][digit] == col[digit][j] == block[i//3][j//3][digit] == False:
                    row[i][digit] = col[digit][j] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    # backtrace
                    row[i][digit] = col[digit][j] = block[i // 3][j // 3][digit] = False
                if valid:
                    return

        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    row[i][digit] = col[digit][j] = block[i//3][j//3][digit] = True

        dfs(0)

sol = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol.solveSudoku(board)

