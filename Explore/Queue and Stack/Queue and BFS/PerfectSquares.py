# BFS
# time: O(n)
# space: O(sqrt(n))
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        perfect_squares = []
        i = 1
        while i**2 <= n:
            perfect_squares.append(i**2)
            i += 1
        level = 0
        curr_lvl_nodes = {n}
        while curr_lvl_nodes:
            level += 1
            temp = set()
            for x in curr_lvl_nodes:
                for y in perfect_squares:
                    if x == y:
                        return level
                    if x < y:
                        break
                    temp.add(x-y)
            curr_lvl_nodes = temp
        return level