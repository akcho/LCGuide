# Two Pointers
def removeDuplicates(self, nums: List[int]) -> int:
    new_tail = 0
    for i in range(len(nums)):
        if nums[i] != nums[new_tail]:
            new_tail += 1
            nums[new_tail] = nums[i]
        return new_tail + 1