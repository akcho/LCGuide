# List operation, O(n^2)
from collections import defaultdict


def singleNumber(self, nums):
    no_duplicate_list = []
    for num in nums:
        if num not in no_duplicate_list:
            no_duplicate_list.append(num)
        else:
            no_duplicate_list.remove(num)
    return no_duplicate_list.pop()


# Hash table, O(n)
def singleNumber2(self, nums):
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1

    for i in hash_table:
        if hash_table[i] == 1:
            return i


# Math, O(n)
def singleNumber3(self, nums):
    return 2 * sum(set(nums)) - sum(nums)


# Bid Manipulation
def singleNumber4(self, nums):
    a = 0
    for num in nums:
        a ^= num
    return a
