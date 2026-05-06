class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min(prices[:i])
            if max_profit < profit:
                max_profit = profit

        return max_profit