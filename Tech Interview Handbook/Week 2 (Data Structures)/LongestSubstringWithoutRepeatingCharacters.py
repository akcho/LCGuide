# sliding window
# time: O(n)
# space: O(26, n), where n is the size of the string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(lambda: None)
        start = 0
        max_length = 0

        for i, c in enumerate(s):
            if seen[c] is not None:
                if seen[c] >= start:
                    start = seen[c] + 1  # seen[c] contains index
            max_length = max(max_length, i - start + 1)
            seen[c] = i
        return max_length
