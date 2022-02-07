# sliding window (two pointers)
# time: O(s + t)
# space: O(s + t)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_still_needed = Counter(t)
        left, right = 0, 0
        PLACEHOLDER_VAL = len(s) + 1
        min_win_length = PLACEHOLDER_VAL
        min_win_start = 0
        total_chars_still_needed = len(t)

        while right < len(s):
            right_char = s[right]
            if right_char in chars_still_needed:
                chars_still_needed[right_char] -= 1
                if chars_still_needed[right_char] >= 0:
                    total_chars_still_needed -= 1


            while total_chars_still_needed == 0:
                curr_win_length = right - left + 1
                if curr_win_length < min_win_length:
                    min_win_length = curr_win_length
                    min_win_start = left

                left_char = s[left]
                if left_char in chars_still_needed:
                    chars_still_needed[left_char] += 1
                    if chars_still_needed[left_char] > 0:
                        total_chars_still_needed += 1
                left += 1

            right += 1

        if min_win_length == len(s) + 1:
            return ""
        else:
            return s[min_win_start:min_win_start + min_win_length]
