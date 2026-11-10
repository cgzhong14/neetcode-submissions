class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0
        while(sell < len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                current = prices[sell] - prices[buy]
                profit = max(profit, current)
            sell+=1
        return profit