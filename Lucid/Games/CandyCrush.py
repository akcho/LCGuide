# two pointers (wr is a write row)
# time: O((R * C)^2), we need O(R*C) to scan the board and might need to crush 3 every time
# space: O(1), we edit the board in place

class Solution(object):
    def candyCrush(self, board):
        num_rows, num_cols = len(board), len(board[0])
        todo = False

        for r in range(num_rows):
            for c in range(num_cols - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                    todo = True

        for r in range(num_rows - 2):
            for c in range(num_cols):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                    todo = True

        # update board for gravity
        for c in range(num_cols):
            wr = num_rows - 1
            # add unmodified cells while keeping track of when the 0s should start
            for r in reversed(range(num_rows)):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1

            # populate all remaining cells above wr with 0
            for wr in reversed(range(wr + 1)):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board