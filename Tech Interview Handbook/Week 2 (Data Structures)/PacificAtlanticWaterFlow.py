# BFS
#time: O(m*n)
# space: O(m*n)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        matrix = heights

        if not matrix or not matrix[0]:
            return []

        num_rows, num_cols = len(matrix), len(matrix[0])

        pacific_q = deque()
        atlantic_q = deque()

        for i in range(num_rows):
            pacific_q.append((i, 0))
            atlantic_q.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_q.append((0, i))
            atlantic_q.append((num_rows - 1, i))

        def bfs(q):
            reachable = set()
            while q:
                (row, col) = q.popleft()
                reachable.add((row, col))

                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row, new_col = row + x, col + y

                    # skip (continue to next loop) if out of bounds
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue

                    if (new_row, new_col) in reachable:
                        continue

                    # skip if new cell is too short
                    if matrix[row][col] > matrix[new_row][new_col]:
                        continue

                    q.append((new_row, new_col))
            return reachable

        pacific_reachable = bfs(pacific_q)
        atlantic_reachable = bfs(atlantic_q)

        return list(pacific_reachable.intersection(atlantic_reachable))
