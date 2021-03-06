# Two Pointers
# Time: O(n^2)
# Space: O(n) -> technically O(log n) + O(n) bc of sorting

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # Since we sorted, res should be completely filled by the time we reach the first positive int
            if nums[i] > 0:
                break

            # The if statement below is tricky. Here's what's important:
            # 1. i == 0 is there so we don't break from looking at nums[i-1] in the second condition
            # 2. we want to run twoSum on non-identical consecutive nums bc we don't want duplicate triplets
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, i, res):
        # set up two pointers
        lo, hi = i + 1, len(nums) - 1

        while lo < hi:
            sum_ = nums[i] + nums[lo] + nums[hi]
            # goldilocks using two pointers until sum_ == 0
            if sum_ < 0:
                lo += 1
            elif sum_ > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                # This final while loop is to remove duplicate scenarios (similar logic as main func)
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1