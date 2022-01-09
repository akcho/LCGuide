# BFS
# time: O(mn)
# space: O(mn)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms: return

        EMPTY = 2 ** 31 - 1
        GATE = 0
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows = len(rooms)
        cols = len(rooms[0])
        q = deque()

        # queue starts with gate coords but will also include revised (prev empty) cells
        for row in range(rows):
            for col in range(cols):
                # add gate to queue
                if rooms[row][col] == GATE:
                    q.append([row, col])

        # BFS
        while len(q) != 0:
            popped_row, popped_col = q.popleft()
            for direction in DIRECTIONS:
                r = popped_row + direction[0]
                c = popped_col + direction[1]
                if 0 <= r < rows and 0 <= c < cols and rooms[r][c] == EMPTY:
                    rooms[r][c] = rooms[popped_row][popped_col] + 1
                    q.append([r, c])





