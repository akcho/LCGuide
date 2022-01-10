# BFS
# time: O(N**2 * A**N (# of letters in alphabet to the Nth power) + D (instantiate Deadend))
# space: O(A**N + D) for the queue and the set dead
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(combo):
            # loop through each wheel
            for i in range(4):
                digit = int(combo[i])
                for direction in (-1, 1):
                    # modulo if it hits 10 (eg. 0 would go back to 9 instead of -1)
                    neighbor = (digit + direction) % 10

                    # only return digit as diff in combo str
                    yield combo[:i] + str(neighbor) + combo[i+1:]

        dead = set(deadends)
        queue = deque([('0000', 0)])
        seen = {'0000'}

        while queue:
            combo, num_turns = queue.popleft()
            if combo == target:
                return num_turns
            if combo in dead: continue

            for nei in neighbors(combo):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, num_turns + 1))
        return -1
