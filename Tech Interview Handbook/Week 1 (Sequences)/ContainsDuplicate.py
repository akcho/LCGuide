# Brute Force
# Time complexity: O(n^2)
# Space complexity: O(1)
def containsDuplicate(self, nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Sorting
# Time complexity: O (n log n)
# Space complexity: O(1)
def containsDuplicate2(self, nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Hash Set
# Time complexity: O(n)
# Space complexity: O(n)
def containsDuplicate3(self, nums):
    set_ = set()
    for num in nums:
        if num in set_:
            return True
        set_.add(num)
    return False