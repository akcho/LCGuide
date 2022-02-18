# Iterative DFS
# time: O(1) bc they tell us it's 8x8
# space: O(1)

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        n = 0
        num_rows, num_cols = len(board), len(board[0])
        WHITE = "W"
        BLACK = "B"
        EMPTY = "."
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        board[rMove][cMove] = color

        def legal(row, col, color, direction):
            dr, dc = direction
            row, col = row + dr, col + dc
            length = 1

            while (0 <= row < num_rows and 0 <= col < num_cols):
                length += 1
                if board[row][col] == EMPTY: return False

                # check if a newly encountered color is same as the starting point
                if board[row][col] == color: return length >= 3
                row, col = row + dr, col + dc
            return False

        for d in directions:
            if legal(rMove, cMove, color, d): return True
        return False
