# sliding window
# time: O(n)
# space: O(26, n), where n is the size of the string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = defaultdict(lambda: None)
        win_start = 0
        best_win_length = 0

        for i, c in enumerate(s):
            # if we've seen c before within our current window:
            if last_seen[c] is not None and last_seen[c] >= win_start:
                # Reset our window to start right after this repeated c's index.
                win_start = last_seen[c] + 1

            curr_win_length = i - win_start + 1
            best_win_length = max(best_win_length, curr_win_length)
            last_seen[c] = i
        return best_win_length

