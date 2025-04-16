class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_price = prices[0]
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] > max_price:
                max_price = prices[i]
                profit = max(profit, max_price - min_price)
            elif prices[i] < min_price:
                min_price = prices[i]
                max_price = prices[i]

        return profit
