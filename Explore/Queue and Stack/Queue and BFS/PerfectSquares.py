# BFS
# time: O(n)
# space: O(sqrt(n))
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        i = 1
        while i ** 2 <= n:
            perfect_squares.append(i ** 2)
            i += 1

        level = 0
        curr_lvl_nodes = {n}
        while curr_lvl_nodes:
            level += 1
            temp = set()
            for node in curr_lvl_nodes:
                for ps in perfect_squares:
                    if node == ps:
                        return level
                    if node < ps:
                        break
                    temp.add(node - ps)
            curr_lvl_nodes = temp
        return level