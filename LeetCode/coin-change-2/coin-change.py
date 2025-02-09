from functools import cache
from typing import List, Tuple

class Solution:
    
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def change_help(self, amount: int, coins: Tuple[int]) -> int:
            if amount == 0:
                return 1
            if amount < 0 or coins == ():
                return 0
            combs = 0
            for n in range(amount//coins[0] + 1):
                combs += self.change_help(amount - n * coins[0], coins[1:])
            return combs

        return change_help(amount, tuple(coins))
        
class Solution2:

    def change(self, amount: int, coins: List[int]) -> int:
        n_coins = len(coins)
        @cache
        def change_help(self, x: int, i: int) -> int:
            if x == 0:
                return 1
            if x < 0 or i > n_coins:
                return 0
            combs = 0
            for n in range(x//coins[i] + 1):
                combs += self.change_help(x - n * coins[i], i + 1)
            return combs
        return change_help(amount, 0)
