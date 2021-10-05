# Brute Force
# Time: O(n * k)
# Space: O(1)
from typing import List


def rotate(self, nums, k):
    k %= len(nums)
    for i in range(k):
        prev = nums[-1]
        for j in range(len(nums)):
            nums[j], prev = prev, nums[j]


# Extra Array
# Time: O(n)
# Space: O(n)
def rotate2(self, nums, k):
    n = len(nums)
    a = [0] * n
    for i in range(n):
        a[(i + k) % n] = nums[i]

    nums[:] = a


# Cyclic Replacements
# Time: O(n)
# Space: O(1)
def rotate4(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n

    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1

            if start == current:
                break
        start += 1


# Using Reverse
# Time: O(n)
# Space: O(1)
def reverse(self, nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate3(self, nums, k):
    k %= len(nums)
    n = len(nums) - 1
    self.reverse(nums, 0, n)
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, n)
