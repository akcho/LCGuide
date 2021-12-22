# time: O(n)
# space: O(min(m,n))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        i_map = {}

        i = 0
        for j in range(len(s)):
            curr_char = s[j]
            if curr_char in i_map:
                i = max(i_map[curr_char], i)
            answer = max(answer, j - i + 1)
            i_map[curr_char] = j + 1

        return answer