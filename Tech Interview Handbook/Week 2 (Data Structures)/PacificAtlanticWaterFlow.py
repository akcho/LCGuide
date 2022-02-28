# BFS
#time: O(rows * cols)
# space: O(rows * cols))

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        matrix = heights
        if not matrix or not matrix[0]: return []

        num_rows, num_cols = len(matrix), len(matrix[0])
        pq, aq = deque(), deque()

        for i in range(num_rows):
            pq.append((i, 0))
            aq.append((i, num_cols - 1))
        for i in range(num_cols):
            pq.append((0, i))
            aq.append((num_rows - 1, i))

        def bfs(q):
            will_flow_down = set()
            while q:
                r, c = q.popleft()
                will_flow_down.add((r, c))

                for (dr, dc) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if not 0 <= nr < num_rows or not 0 <= nc < num_cols: continue
                    if (nr, nc) in will_flow_down: continue

                    # Remember: we start on the coast, and bfs toward the center
                    if matrix[nr][nc] < matrix[r][c]: continue
                    q.append((nr, nc))
            return will_flow_down

        fp = bfs(pq)
        fa = bfs(aq)

        return fp & fa

