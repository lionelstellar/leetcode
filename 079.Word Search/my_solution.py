## exceed time
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        raw = len(board)
        col = len(board[0])
        choosen = [[False] * col for _ in range(raw)]
        for x in range(col):
            for y in range(raw):
                if self.check(board, choosen, word, x, y, x, y):
                    return True
        return False

    def deepcopy(self, choosen):
        raw = len(choosen)
        col = len(choosen[0])
        ret = [[False] * col for _ in range(raw)]
        for x in range(col):
            for y in range(raw):
                if choosen[y][x]:
                    ret[y][x] = True
        return ret

    def check_cord(self, x, y, board):
        raw = len(board)
        col = len(board[0])
        return 0 <= x < col and 0 <= y < raw

    def check(self, board, choosen, word, x_ori, y_ori, x, y):
        if word == "":
            return True

        revert_flag = False
        if x_ori == x + 1 and y_ori == y:
            revert_flag = True

        if self.check_cord(x, y, board) and choosen[y][x] == False:
            if board[y][x] == word[0]:
                new_choosen = self.deepcopy(choosen)
                new_choosen[y][x] = True
                word = word[1:]
                return self.check(board, new_choosen, word, x, y, x, y + 1) or \
                    self.check(board, new_choosen, word, x, y, x, y - 1) or \
                    self.check(board, new_choosen, word, x, y, x + 1, y) or \
                    self.check(board, new_choosen, word, x, y, x - 1, y)



board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word = "AAAAAAAAAAAAAAB"
sol = Solution()
print(sol.exist(board, word))