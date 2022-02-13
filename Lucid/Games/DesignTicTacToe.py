# Almost identical to FindWinner. Just in a class modeling format
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row_sums = [0] * n
        self.col_sums = [0] * n
        self.diag = 0
        self.anti_diag = 0

    # time: O(1)
    # space: O(n) <- all kept in init
    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        p_id = 1
        if player == 2: p_id = -1

        self.row_sums[row] += p_id
        self.col_sums[col] += p_id

        if row == col:
            self.diag += p_id
        if row + col == n - 1:
            self.anti_diag += p_id

        for sum_ in (self.row_sums[row], self.col_sums[col], self.diag, self.anti_diag):
            if abs(sum_) == n:
                return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)