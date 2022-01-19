# sliding window (two pointers)
# time: O(s + t)
# space: O(s + t)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_still_needed = Counter(t)
        left, right = 0, 0
        min_window_length = len(s) + 1
        min_window_start = 0
        total_chars_still_needed = len(t)

        while right < len(s):
            right_char = s[right]
            if right_char in chars_still_needed:
                if chars_still_needed[right_char] > 0:
                    total_chars_still_needed -= 1
                chars_still_needed[right_char] -= 1

            while total_chars_still_needed == 0:
                if right - left + 1 < min_window_length:
                    min_window_length = right - left + 1
                    min_window_start = left

                left_char = s[left]
                if left_char in chars_still_needed:
                    if chars_still_needed[left_char] >= 0:
                        total_chars_still_needed += 1
                    chars_still_needed[left_char] += 1
                left += 1

            right += 1

        if min_window_length == len(s) + 1:
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_length]
