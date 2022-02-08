# BFS
#time: O(rows * cols)
# space: O(rows * cols))

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        matrix = heights

        # remove null cases
        if not matrix or not matrix[0]:
            return []

        num_rows, num_cols = len(matrix), len(matrix[0])
        pacific_q, atlantic_q = deque(), deque()

        # add "coasts" (edges of matrix) to their respective oceans
        for i in range(num_rows):
            pacific_q.append((i, 0))
            atlantic_q.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_q.append((0, i))
            atlantic_q.append((num_rows - 1, i))

        def bfs(q):
            # will_flow_down will only contain coords that water can "flow down" from and to
            will_flow_down = set()
            while q:
                (row, col) = q.popleft()
                will_flow_down.add((row, col))

                # check neighbors using BFS
                for (dir_r, dir_c) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    neighboring_r, neighboring_c = row + dir_r, col + dir_c

                    # don't add if out of bounds
                    if neighboring_r < 0 or neighboring_r >= num_rows :
                        continue
                    if neighboring_c < 0 or neighboring_c >= num_cols:
                        continue

                    # don't add if already added to set of flowable cells
                    if (neighboring_r, neighboring_c) in will_flow_down:
                        continue

                    # don't add if neighboring cell is too short for water to flow down from
                    if matrix[neighboring_r][neighboring_c]  < matrix[row][col]:
                        continue

                    q.append((neighboring_r, neighboring_c))
            return will_flow_down

        flow_to_pacific = bfs(pacific_q)
        flow_to_atlantic = bfs(atlantic_q)

        return flow_to_pacific.intersection(flow_to_atlantic)  # also write as "flow_to_pacific & flow_to_atlantic"
