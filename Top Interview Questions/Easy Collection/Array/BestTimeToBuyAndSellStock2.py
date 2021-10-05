from typing import List

# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n), where n is depth of recursion
def maxProfit(self, prices: List[int]) -> int:
    return self.calculate(prices, 0)


def calculate(self, prices, s):
    if s >= len(prices):
        return 0
    max = 0
    for start in range(s, len(prices)):
        maxprofit = 0
        for i in range(start + 1, len(prices)):
            if prices[start] < prices[i]:
                profit = self.calculate(prices, i + 1) + prices[i] - prices[start]
                if profit > maxprofit:
                    maxprofit = profit
        if maxprofit > max:
            max = maxprofit
    return max


# Peak Valley Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def maxProfit2(self, prices):
    i = 0
    valley = prices[0]
    peak = prices[0]
    maxprofit = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i+1]:
            i += 1
        valley = prices[i]
        while i < len(prices) - 1 and prices[i] <= prices[i+1]:
            i += 1
        peak = prices[i]
        maxprofit += peak - valley
    return maxprofit


# Time Complexity: O(n)
# Space Complexity: O(1)
def maxProfit3(self, prices) -> int:
    total = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            total += prices[i + 1] - prices[i]
    return total
