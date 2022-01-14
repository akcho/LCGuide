# stack
# time: O(n)
# space: O(n)

class Solution:
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        for curr_idx, curr_temp in enumerate(T):
            while stack and T[stack[-1]] < curr_temp:
                prev_idx = stack.pop()
                ans[prev_idx] = curr_idx - prev_idx
            stack.append(curr_idx)

        return ans