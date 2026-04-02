class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buying_price = prices[0]
        for i in range(len(prices)):
            if buying_price > prices[i]:
                buying_price = prices[i]
            if buying_price < prices[i]:
                profit = max(profit, prices[i]-buying_price)

        return profit

            




        