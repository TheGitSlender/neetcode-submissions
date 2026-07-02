class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < min:
                min = prices[i]
            current_profit = prices[i] - min
            if current_profit > profit:
                profit = current_profit
        
        return profit
