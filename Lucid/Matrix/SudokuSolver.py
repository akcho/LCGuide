# backtracking
# time: Technically constant, but 9! ^ 9, so crazy big
# space: O(81)

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def find_unassigned(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '.': return r, c
        return -1, -1

    def get_range(self, x):
        x -= x % 3
        return range(x, x + 3)

    def is_safe(self, r, c, num):
        row_safe = all(self.board[r][i] != num for i in range(9))
        col_safe = all(self.board[i][c] != num for i in range(9))
        square_safe = all(self.board[i][j] != num for i in self.get_range(r) for j in self.get_range(c))
        return row_safe and col_safe and square_safe

    def solve(self):
        r, c = self.find_unassigned()
        if (r, c) == (-1, -1): return True

        for num in map(str, range(1, 10)):
            if self.is_safe(r, c, num):
                self.board[r][c] = num
                if self.solve():
                    return True
                else:
                    self.board[r][c] = '.'