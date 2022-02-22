# BFS (shortest path)
# time: O(m * n * k), k == number of lives
# space: O(m * n * k)

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        lives_grid = [[-1 for c in range(num_cols)] for r in range(num_rows)]
        q = deque()
        q.append([0, 0, k, 0])

        while len(q) > 0:
            r, c, lives, dist = q.popleft()
            if r == num_rows - 1 and c == num_cols - 1:
                return dist

            if grid[r][c] == 1:
                lives -= 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols and lives_grid[nr][nc] < lives:
                    q.append([nr, nc, lives, dist + 1])
                    lives_grid[nr][nc] = lives
        return -1