class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        b = 0
        for i in range(1, len(prices)):
            if prices[b] < prices[i]:
                max_profit = max(max_profit, prices[i] - prices[b])
            else:
                b = i

        return max_profit