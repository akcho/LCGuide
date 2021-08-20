# Brute Force
def rotate(self, nums, k):
    k %= len(nums)
    for i in range(k):
        prev = nums[-1]
        for j in range(len(nums)):
            nums[j], prev = prev, nums[j]


# Extra Array
def rotate2(self, nums, k):
    n = len(nums)
    a = [0] * n
    for i in range(n):
        a[(i + k) % n] = nums[i]

    nums[:] = a


# Using Reverse
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
