class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        '''
        for i in range(len(coins)):
            for a in range(1, amount + 1):
                if a - coins[i] >= 0:
                    dp[a] += dp[a - coins[i]]
        '''
        return dp[amount]

class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*len(coins) for i in range(amount + 1)]
        for i in range(len(coins)):
            dp[0][i] = 1
            for a in range(1, amount + 1):
                if i - 1 >= 0:
                    dp[a][i] += dp[a][i - 1] 
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][len(coins) - 1]


class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def recurse(amt, i):
            if amt == 0:
                return 1
            if i >= len(coins):
                return 0
            res = 0
            if amt - coins[i] >= 0:
                res += recurse(amt - coins[i], i)
            res += recurse(amt, i + 1)
            return res
        return recurse(amount, 0)
