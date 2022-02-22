# hash map to track scores for row, col, square
# time: O(1)
# space: O(m * n)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        num_rows, num_cols = len(board), len(board[0])

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue

                if board[r][c] in rows[r]: return False
                if board[r][c] in cols[c]: return False
                if board[r][c] in squares[(r // 3, c // 3)]: return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True