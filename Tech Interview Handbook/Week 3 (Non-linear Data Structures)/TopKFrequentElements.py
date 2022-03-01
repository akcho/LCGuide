# bucket sort
# time: O(n) -> O(n) to populate array, O(n) to go through array
# space: O(n) -> O(n) for array, O(n) for counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)

        for val, count in count.items(): freq[count].append(val)

        res = []
        for i in reversed(range(len(freq))):
            for val in freq[i]:
                res.append(val)
                if len(res) == k: return res
