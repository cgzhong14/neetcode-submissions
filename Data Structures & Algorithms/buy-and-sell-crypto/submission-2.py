class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        left = 0  # Buy pointer
        right = 1  # Sell pointer
        max_profit = 0
        
        while right < len(prices):
            # If we found a profitable transaction
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # If right price is lower, move left pointer to right
                # (found a better buying opportunity)
                left = right
            
            # Always move right pointer forward
            right += 1
        
        return max_profit