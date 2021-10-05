# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    slow_runner = 0
    for fast_runner in range(len(nums)):
        if nums[fast_runner] != nums[slow_runner]:
            slow_runner += 1
            nums[slow_runner] = nums[fast_runner]
    return slow_runner + 1
