from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = ceil(sum(piles) / h)
        l = 1
        r = max(piles)
        while l < r:
            k = (l + r) // 2
            time = sum(ceil(pile/k) for pile in piles)
            if time > h:
                l = k + 1
            else:
                r = k
        return l
