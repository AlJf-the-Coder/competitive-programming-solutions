class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_1 = buy_2 = sell = 0
        
        for i in range(len(prices) - 1, -1, -1):
            tmp = buy_1
            buy_1 = max(buy_1, sell - prices[i])
            sell = max(sell, buy_2  + prices[i])
            buy_2 = tmp

        return buy_1

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * (len(prices) + 2)
        sell = [0] * (len(prices) + 2)
        
        for i in range(len(prices) - 1, -1, -1):
            buy[i] = max(buy[i + 1], sell[i + 1] - prices[i])
            sell[i] = max(sell[i + 1], buy[i + 2]  + prices[i])

        return buy[0]

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def recurse(buy, i):
            if i >= len(prices):
                return 0

            if buy:
                return max(recurse(buy, i + 1), recurse(not buy, i + 1 ) - prices[i])
            else:
                return max(recurse(buy, i + 1), recurse(not buy, i + 2)  + prices[i])

        return recurse(True, 0)
