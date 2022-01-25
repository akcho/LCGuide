from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our current and max subarrays with the first num in nums.
        curr = max_ = nums[0]

        # Start with the second num since we already initialized with first num.
        for num in nums[1:]:
            # curr does two things:
            # 1. Keeps a running sum
            # 2. Discards a negative curr_subarray if/when we reach a positive num
            curr = max(num, curr + num)

            # max_ stores the best subarray
            max_ = max(max_subarray, current_subarray)

        return max_subarray