# sliding window
# time: O(n)
# space: O(n) -> 26, if we have to store every char in defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win_length = 0
        most_chars_in_win = 0
        win_char_count = defaultdict(int)

        for i, c in enumerate(s):
            win_char_count[c] += 1
            most_chars_in_win = max(most_chars_in_win, win_char_count[c])

            # If we can switch more chars even after increasing curr window:
            if k > win_length - most_chars_in_win:
                # Increment curr window length (this is our officially our best so far)
                win_length += 1

            # Else, we move the left of our window by 1
            else:
                char_at_win_start = s[i - win_length]
                # Decrement the count of curr window's starting char in our hash set.
                # This is like moving the left pointer in a traditional sliding window.
                win_char_count[char_at_win_start] -= 1
        return win_length