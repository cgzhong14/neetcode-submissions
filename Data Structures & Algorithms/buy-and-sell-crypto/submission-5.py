class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        l = 0
        r = 1
        maxProfit = 0
        while(r < len(prices)):
            tempProfit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            else:
                maxProfit = max(tempProfit, maxProfit)
            r+=1

        return maxProfit