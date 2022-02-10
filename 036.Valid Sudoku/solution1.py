class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # judge rows and cols
        for i in range(9):
            for j in range(9):
                for k in range(j + 1, 9):
                    if board[i][j] == board[i][k] and board[i][j] != ".":
                        return False

                    if board[j][i] == board[k][i] and board[j][i] != ".":
                        return False

        # judge 3 * 3 sub-boxes
        square = []
        for i in range(3):
            for j in range(3):
                tmp = []
                for m in range(3):
                    for n in range(3):
                        if board[3 * i + m][3 * j + n] != ".":
                            tmp.append(board[3 * i + m][3 * j + n])
                square.append(tmp)

        for i in range(9):
            for j in range(len(square[i])):
                for k in range(j + 1, len(square[i])):
                    if square[i][j] == square[i][k]:
                        return False

        return True



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

print(sol.isValidSudoku(board))

