class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = []
        profit = 0
        for i in range(len(prices) - 1):
            arr.append(max(prices[i + 1: len(prices)]))
        for i in range(len(prices) - 1):
            profit = max(profit, arr[i] - prices[i])
        return profit
