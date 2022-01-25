from typing import List

# Time: O(n)
# Space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1] * len(nums)

        # Set a[i] as the product of all elements left of i
        for i in range(1, len(nums)):
            a[i] = a[i - 1] * nums[i - 1]  # a[i-1] is a running product

        r = 1
        # make r the product of all elements right of i.
        # multiply r with products of left elements to get the product of all elements on either side of i
        for i in reversed(range(len(nums))):
            a[i] *= r
            r *= nums[i]

        return a