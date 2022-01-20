# expand around all possible centers
# time: O(n^2)
# space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_around_center(s, low, high):
            ans = 0
            while low >= 0 and high < len(s):
                if s[low] != s[high]:
                    break
                low -= 1
                high += 1
                ans += 1
            return ans

        ans = 0
        for i in range(len(s)):
            # for odd palindromes
            ans += count_around_center(s, i, i)

            # for even palindromes
            ans += count_around_center(s, i, i + 1)

        return ans