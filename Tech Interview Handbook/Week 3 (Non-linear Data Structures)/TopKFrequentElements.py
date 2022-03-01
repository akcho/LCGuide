# bucket sort
# time: O(n) -> O(n) to populate array, O(n) to go through array
# space: O(n) -> O(n) for array, O(n) for counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        count = Counter(nums)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in reversed(range(len(freq))):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: return res