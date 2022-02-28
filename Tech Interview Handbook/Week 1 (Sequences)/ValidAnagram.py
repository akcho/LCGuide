# hashmap
# time: O(n)
# space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}

        for char in s:
            if char not in hm:
                hm[char] = 1
            else:
                hm[char] += 1

        for char in t:
            if char not in hm:
                return False
            else:
                hm[char] -= 1

        for h in hm:
            if hm[h] != 0: return False
        return True