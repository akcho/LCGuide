# recursive DFS
# time: O(n * m * 4^w) -> n = length, m = width, w = word length
# space: O(1)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols = len(board), len(board[0])
        VISITED = '-1'

        def dfs(r, c, i):
            if i == len(word): return True

            if not 0 <= r < num_rows or not 0 <= c < num_cols: return False
            if word[i] != board[r][c]: return False
            if (r, c) in path: return False

            og_val = board[r][c]
            board[r][c] = VISITED
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c - 1, i + 1) or
                   dfs(r, c + 1, i + 1))
            board[r][c] = og_val
            return res

        for row in range(num_rows):
            for col in range(num_cols):
                if dfs(row, col, 0): return True
        return False
