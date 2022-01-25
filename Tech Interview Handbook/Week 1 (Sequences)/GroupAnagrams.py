# default dict
# Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs.
# Space Complexity: O(NK), the total information content stored in ans.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()