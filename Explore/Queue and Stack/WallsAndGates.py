# BFS
# time: O(mn)
# space: O(mn)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        EMPTY = 2 ** 31 - 1
        GATE = 0
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        m = len(rooms)
        if m == 0: return
        n = len(rooms[0])
        q = deque()

        for row in range(m):
            for col in range(n):
                if rooms[row][col] == GATE:
                    q.append([row, col])

        while len(q) != 0:
            point = q.popleft()
            row = point[0]
            col = point[1]
            for direction in DIRECTIONS:
                r = row + direction[0]
                c = col + direction[1]
                if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != EMPTY:
                    continue
                rooms[r][c] = rooms[row][col] + 1
                q.append([r, c])


