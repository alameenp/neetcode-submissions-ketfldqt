class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        max_profit = 0
        buy = float('inf')
        bought_at = 0
        for i,price in enumerate(prices):
            if buy > price:
                buy = price
                bought_at = i
                continue
            profit = max(price - buy,0)
            if profit > 0:
                max_profit = max(profit,max_profit)
        return max_profit


                
            




            
            
            

        