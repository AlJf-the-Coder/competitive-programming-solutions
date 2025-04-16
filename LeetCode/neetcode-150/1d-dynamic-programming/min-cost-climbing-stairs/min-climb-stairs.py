class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = 0, 0
        for i in range(2, n + 1):
            one, two = two, min(one + cost[i - 2], two + cost[i - 1])
        return two

class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def help(i):
            if i < 2: 
                return 0
            return min(help(i - 1) + cost[i - 1], help(i - 2) + cost[i - 2])
        return help(n)
