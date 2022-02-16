class UltimateTicTacToe:
    def __init__(self):
        self.rows = [TicTacToe(3)] * 3
        self.cols = [TicTacToe(3)] * 3
        self.curr_board = (-1,-1)

    def move(self, row, col, player):
        

        if self.curr_board == (-1,-1):
            self.curr_board = (row, col)

        self.curr_board.move(row, col, player)



# Almost identical to FindWinner. Just in a class modeling format
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row_sums = [0] * 3
        self.col_sums = [0] * 3
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


if __name__ == "__main__":
    test = UltimateTicTacToe()
