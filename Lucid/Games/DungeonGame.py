# dynamic programming
# time: O(m*n)
# space: O(m*n)

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon: return 0

        # create HP table
        hp = [[0 for c in range(len(dungeon[r]))] for r in range(len(dungeon))]
        hp[-1][-1] = 1 if dungeon[-1][-1] > 0 else (abs(dungeon[-1][-1]) + 1)

        # fill right column
        for r in reversed(range(len(hp) - 1)):  # start in cell above last
            curr = dungeon[r][-1]
            if curr > 0:
                hp[r][-1] = max(1, hp[r + 1][-1] - curr)
            elif curr <= 0:
                hp[r][-1] = hp[r + 1][-1] + abs(curr)

        # fill bottom row
        for c in reversed(range(len(hp[-1]) - 1)):  # start in cell left of last
            curr = dungeon[-1][c]
            if curr > 0:
                hp[-1][c] = max(hp[-1][c + 1] - curr, 1)
            elif curr <= 0:
                hp[-1][c] = hp[-1][c + 1] + abs(curr)

        # fill rest of table
        for r in reversed(range(len(hp) - 1)):
            for c in reversed(range(len(hp[-1]) - 1)):
                curr = dungeon[r][c]
                cheaper_cell = min(hp[r][c + 1], hp[r + 1][c])
                if curr > 0:
                    hp[r][c] = max(cheaper_cell - curr, 1)
                elif curr <= 0:
                    hp[r][c] = cheaper_cell + abs(curr)

        return hp[0][0]
