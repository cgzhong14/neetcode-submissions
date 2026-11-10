class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = 0
        sell = 1
        profit = 0
        while(sell != len(prices)):
            if prices[buy] < prices[sell]:
                currentProfit = prices[sell] - prices[buy]
                profit = max(currentProfit,profit)
            else:
                buy = sell
            sell+=1
        return profit