# recursive DFS
# time: O(m*n)
# space: O(m*n) <- hash set could contain every cell in grid

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LAND = 1
        WATER = 0
        VISITED = -1
        num_rows, num_cols = len(grid), len(grid[0])

        def dfs(r, c):
            if not 0 <= r < num_rows or not 0 <= c < num_cols: return 0
            if grid[r][c] != LAND: return 0

            grid[r][c] = VISITED
            return (1 + dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))

        area = 0
        for r in range(num_rows):
            for c in range(num_cols):
                area = max(area, dfs(r, c))

        return area