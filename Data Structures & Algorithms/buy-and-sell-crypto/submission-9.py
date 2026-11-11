class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        L = 0
        profit = 0
        for R in range(len(prices)):
            cur = prices[R] - prices[L]
            profit = max(profit, cur)
            if cur < 0:
                L = R
        return profit