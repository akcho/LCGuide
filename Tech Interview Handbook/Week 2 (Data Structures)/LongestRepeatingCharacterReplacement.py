# sliding window
# time: O(n)
# space: O(n) -> 26, if we have to store every char in defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_win_size = 0
        most_chars_in_win = 0
        win_char_count = defaultdict(int)

        for i, c in enumerate(s):
            win_char_count[c] += 1
            most_chars_in_win = max(most_chars_in_win, win_char_count[c])

            if k > max_win_size - most_chars_in_win:
                max_win_size += 1
            else:
                win_start = s[i - max_win_size]
                win_char_count[win_start] -= 1
        return max_win_size