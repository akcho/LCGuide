# DFS
# time: O(1)
# space: O(1)
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        num_rows, num_cols = len(board), len(board[0])
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        def get_adjacent_mines(r, c):
            num_mines = 0
            for nr in range(r - 1, r + 2):
                for nc in range(c - 1, c + 2):
                    if 0 <= nr < num_rows and 0 <= nc < num_cols:
                        if board[nr][nc] == 'M':
                            num_mines += 1
            return num_mines

        def dfs(r, c):
            if board[r][c] != 'E': return

            num_mines = get_adjacent_mines(r, c)
            if num_mines > 0:
                board[r][c] = str(num_mines)
                return
            else:
                board[r][c] = 'B'
                for nr in range(r - 1, r + 2):
                    for nc in range(c - 1, c + 2):
                        if 0 <= nr < num_rows and 0 <= nc < num_cols:
                            dfs(nr, nc)

        dfs(r, c)
        return board

