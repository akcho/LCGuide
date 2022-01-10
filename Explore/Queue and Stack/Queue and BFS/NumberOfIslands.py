# BFS
# time: O(mn)
# space: O(min(m,n))

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        LAND = '1'
        WATER = '0'
        VISITED = '-1'

        num_rows = len(grid)
        num_cols = len(grid[0])

        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == LAND:
                    num_islands += 1
                    grid[r][c] = VISITED
                    neighbors = deque()
                    neighbors.append([r, c])
                    while neighbors:
                        row, col = neighbors.popleft()
                        up = row - 1
                        down = row + 1
                        left = col - 1
                        right = col + 1

                        up_in_bounds = (up >= 0)
                        down_in_bounds = (down < num_rows)
                        left_in_bounds = (left >= 0)
                        right_in_bounds = (right < num_cols)

                        if up_in_bounds and grid[up][col] == LAND:
                            neighbors.append([up, col])
                            grid[up][col] = VISITED
                        if down_in_bounds and grid[down][col] == LAND:
                            neighbors.append([down, col])
                            grid[down][col] = VISITED
                        if left_in_bounds and grid[row][left] == LAND:
                            neighbors.append([row, left])
                            grid[row][left] = VISITED
                        if right_in_bounds and grid[row][right] == LAND:
                            neighbors.append([row, right])
                            grid[row][right] = VISITED
        return num_islands

print("test")