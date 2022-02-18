# BFS
# time: O(m*n)
# space: O(m*n)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        q = deque()
        time, fresh = 0, 0

        num_rows, num_cols = len(grid), len(grid[0])
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == FRESH:
                    fresh += 1
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row, col = r + dr, c + dc
                    # if in bounds and fresh, make rotten
                    if (0 <= row < num_rows and
                            0 <= col < num_cols and
                            grid[row][col] == FRESH):
                        grid[row][col] = ROTTEN
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1