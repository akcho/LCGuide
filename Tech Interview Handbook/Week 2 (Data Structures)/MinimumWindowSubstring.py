# sliding window (two pointers)
# time: O(s + t)
# space: O(s + t)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_win_start = 0
        PLACEHOLDER_VAL = len(s) + 1
        min_win_length = PLACEHOLDER_VAL
        left = 0
        right = 0
        total_chars_left = len(t)
        chars_left = Counter(t)

        while right < len(s):
            right_char = s[right]
            if right_char in chars_left:
                if chars_left[right_char] > 0:
                    total_chars_left -= 1
                chars_left[right_char] -= 1

            while total_chars_left == 0:
                curr_win_length = right - left + 1
                if curr_win_length < min_win_length:
                    min_win_length = curr_win_length
                    min_win_start = left

                left_char = s[left]
                if left_char in chars_left:
                    chars_left[left_char] += 1
                    if chars_left[left_char] > 0:
                        total_chars_left += 1
                left += 1
            right += 1

        if min_win_length == PLACEHOLDER_VAL: return ""
        return s[min_win_start:min_win_start + min_win_length]