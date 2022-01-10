# BFS
# time: O(N**2 * A**N (# of letters in alphabet to the Nth power) + D (instantiate Deadend))
# space: O(A**N + D) for the queue and the set dead
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(combo):
            for i in range(4):
                digit = int(combo[i])
                for direction in (-1, 1):
                    # modulo needed for turning 9-0 or 0-9
                    neighboring_digit = (digit + direction) % 10
                    yield combo[:i] + str(neighboring_digit) + combo[i + 1:]

        seen = {"0000"}
        q = deque([("0000", 0)])

        while q:
            combo, num_turns = q.popleft()
            if combo == target: return num_turns
            if combo in deadends: continue

            for neighboring_combo in neighbors(combo):
                if neighboring_combo not in seen:
                    seen.add(neighboring_combo)
                    q.append([neighboring_combo, num_turns + 1])
        return -1