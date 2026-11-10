class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        l = 0
        for r in range(1, len(prices)):
            currentProfit = prices[r] - prices[l]
            profit = max(profit, currentProfit)
            if prices[r] < prices[l]:
                l = r
        return profit