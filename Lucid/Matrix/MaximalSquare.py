# recursive top-down memoization
# time: O(m*n)
# space: O(m*n)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        num_rows, num_cols = len(matrix), len(matrix[0])
        cache = {}  # stores max LENGTH, not area

        def helper(r, c):
            if r >= num_rows or c >= num_cols: return 0

            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == '1':
                    cache[(r, c)] = 1 + min(down, right, diag)
            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2
