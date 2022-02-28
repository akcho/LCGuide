# expand around all possible centers
# time: O(n^2)
# space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_around_center(s, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        res = 0
        for i in range(len(s)):
            # for odd palindromes
            res += count_around_center(s, i, i)

            # for even palindromes
            res += count_around_center(s, i, i + 1)

        return res