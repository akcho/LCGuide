# Recursive DFS
# time: O(m*n)
# space: O(1)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = "1"
        WATER = "0"
        VISITED = "-1"
        num_rows, num_cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (not 0 <= r < num_rows or
                    not 0 <= c < num_cols or
                    grid[r][c] != LAND):
                return

            grid[r][c] = VISITED
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == LAND:
                    num_islands += 1
                    dfs(r, c)

        return num_islands

# BFS
# time: O(mn)
# space: O(min(m,n))
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        LAND = '1'
        WATER = '0'
        VISITED = '-1'  # you could just use WATER instead of VISITED in our code,
                        # but I think VISITED makes BFS easier to follow.

        num_rows = len(grid)
        num_cols = len(grid[0])

        num_islands = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == LAND:
                    num_islands += 1
                    grid[row][col] = VISITED
                    neighbors = deque()
                    neighbors.append([row, col])
                    while neighbors:
                        n_row, n_col = neighbors.popleft()
                        up = n_row - 1
                        down = n_row + 1
                        left = n_col - 1
                        right = n_col + 1

                        up_in_bounds = (up >= 0)
                        down_in_bounds = (down < num_rows)
                        left_in_bounds = (left >= 0)
                        right_in_bounds = (right < num_cols)

                        if up_in_bounds and grid[up][n_col] == LAND:
                            neighbors.append([up, n_col])
                            grid[up][n_col] = VISITED
                        if down_in_bounds and grid[down][n_col] == LAND:
                            neighbors.append([down, n_col])
                            grid[down][n_col] = VISITED
                        if left_in_bounds and grid[n_row][left] == LAND:
                            neighbors.append([n_row, left])
                            grid[n_row][left] = VISITED
                        if right_in_bounds and grid[n_row][right] == LAND:
                            neighbors.append([n_row, right])
                            grid[n_row][right] = VISITED
        return num_islands

