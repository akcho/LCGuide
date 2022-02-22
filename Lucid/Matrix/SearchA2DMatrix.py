# binary search
# time: O(logm + logn)
# space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])

        top, bot = 0, num_rows - 1
        while bot >= top:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break

        if not (bot >= top): return False
        row = (top + bot) // 2

        left, right = 0, num_cols - 1

        while right >= left:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False