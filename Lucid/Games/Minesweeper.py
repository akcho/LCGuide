# recursive DFS for Bs
# time: O(m*n)
# space: O(1)

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        num_rows, num_cols = len(board), len(board[0])

        def get_adjacent_mines(board, r, c):
            num_mines = 0
            for dr in range(r - 1, r + 2):
                for dc in range(c - 1, c + 2):
                    if 0 <= dr < num_rows and 0 <= dc < num_cols:
                        if board[dr][dc] == 'M':
                            num_mines += 1
            return num_mines

        if not board: return board

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            num_mines = get_adjacent_mines(board, r, c)
            if num_mines:
                board[r][c] = str(num_mines)
            else:
                board[r][c] = 'B'
                for dr in range(r - 1, r + 2):
                    for dc in range(c - 1, c + 2):
                        if 0 <= dr < num_rows and 0 <= dc < num_cols:
                            if board[dr][dc] != 'B':
                                self.updateBoard(board, [dr, dc])

        return board