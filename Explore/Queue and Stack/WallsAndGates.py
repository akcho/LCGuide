# BFS
# time: O(mn)
# space: O(mn)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        EMPTY = 2 ** 31 - 1
        GATE = 0
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows = len(rooms)
        if rows == 0: return
        cols = len(rooms[0])
        q = deque()

        for row in range(rows):
            for col in range(cols):
                # add gate to queue
                if rooms[row][col] == GATE:
                    q.append([row, col])

        while len(q) != 0:
            # pop gate coords off
            coord = q.popleft()
            row = coord[0]  # 1 is north, -1 is south
            col = coord[1]  # 1 is east, -1 is west
            for direction in DIRECTIONS:
                r = row + direction[0]
                c = col + direction[1]
                if r < 0 or c < 0 or r >= rows or c >= cols or rooms[r][c] != EMPTY:
                    continue
                rooms[r][c] = rooms[row][col] + 1
                q.append([r, c])