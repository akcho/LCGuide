# time: O(n)
# space: O(n) -> 26, if we have to store every char in defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_size = 0
        max_count = 0
        count = defaultdict(int)

        for i, c in enumerate(s):
            count[c] += 1
            max_count = max(max_count, count[c])

            if k > window_size - max_count:
                window_size += 1
            else:
                # subtract window start's count to slide the window
                count[s[i - window_size]] -= 1
        return window_size
