class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l = 0
        maxPrice = 0
        for r in range(len(prices)):
            maxPrice = max(prices[r]-prices[l], maxPrice)
            if prices[r] < prices[l]:
                l = r
        return maxPrice