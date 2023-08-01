# https://leetcode.com/problems/surrounded-regions/
# Noice sol by neetcode <3
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def capture(row, col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] != "O":
                return
            board[row][col] = "T"
            capture(row + 1, col)
            capture(row - 1, col)
            capture(row, col + 1)
            capture(row, col - 1)
        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row in [0, ROWS - 1] or col in [0, COLS - 1]):
                    capture(row, col)
        # 2. Capture surrounded regions (O -> X)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
        # 3. Uncapture unsurrounded regions (T -> O)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"
