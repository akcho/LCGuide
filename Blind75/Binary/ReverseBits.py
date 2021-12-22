# Let's start with the solution that makes sense to me...
# time: O(1)
# space: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += ((n & 1) << power)
            n = (n >> 1)
            power -= 1
        return ret
