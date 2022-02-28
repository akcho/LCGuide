# sliding window
# time: O(n)
# space: O(26, n), where n is the size of the string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_win_length = 0
        win_start = 0
        last_seen = {}

        for i, c in enumerate(s):
            if c in last_seen and last_seen[c] >= win_start:
                win_start = last_seen[c] + 1
            last_seen[c] = i

            curr_win_length = i - win_start + 1
            best_win_length = max(best_win_length, curr_win_length)

        return best_win_length

