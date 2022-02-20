# hash map to track scores for row, col, square
# time: O(1)
# space: O(m * n)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r//3,c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue
                if (board[r][c] in cols[c] or
                        board[r][c] in rows[r] or
                        board[r][c] in squares[(r // 3, c // 3)]): return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True