# sliding window
# time: O(n)
# space: O(26, n), where n is the size of the string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = defaultdict(lambda: None)
        window_start = 0
        max_length = 0

        for i, c in enumerate(s):
            if last_seen[c] is not None:  # we've seen c before

                # if we've seen c before within curr window, set window_start
                # to right after this repeated c's index.
                if last_seen[c] >= window_start:
                    window_start = last_seen[c] + 1
            max_length = max(max_length, i - window_start + 1)
            last_seen[c] = i
        return max_length

