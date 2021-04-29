class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        def check(board, word, x, y):
            if word == "":
                return True

            if 0 <= x < col and 0 <= y < raw and board[y][x] == word[0]:
                pickout = word[0]
                board[y][x] = "#"
                word = word[1:]
                for x_move, y_move in [(0, 1), (0, -1),  (1, 0), (-1, 0)]:
                    if check(board, word, x + x_move, y + y_move):
                        return True

                board[y][x] = pickout
                word = pickout + word
                return False

            return False


        raw = len(board)
        col = len(board[0])
        for x in range(col):
            for y in range(raw):
                if check(board, word, x, y):
                    return True
        return False



# board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
# word = "AAAAAAAAAAAAAAB"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
sol = Solution()
print(sol.exist(board, word))