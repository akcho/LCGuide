# Brute Force
def containsDuplicates(self, nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            j += 1
            if nums[i] == nums[j]:
                return True
    return False

# Sorting
def containsDuplicates2(self, nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Hash Set
def containsDuplicates3(self, nums):
    set_ = set()
    for num in nums:
        if num in set_:
            return True
        set_.add(num)
    return False