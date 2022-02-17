# BFS
# time: O(m * n)
# space: O(board + q) == O(m*n)

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)

        dir = 1
        a = []
        n = len(board)

        # reorder the board plotted in Boustrophedon style (gross)
        for i in range(n - 1, -1, -1):
            if dir > 0:
                a.append(board[i])
            else:
                a.append(board[i][::-1])
            dir *= -1
        board = a

        def int_to_pos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            return [r, c]

        q = deque()
        q.append([1, 0])  # square, num_moves
        visit = set()

        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = int_to_pos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == length ** 2:
                    return moves + 1
                if next_square not in visit:
                    visit.add(next_square)
                    q.append([next_square, moves + 1])
        return -1
