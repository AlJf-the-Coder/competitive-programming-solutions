class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = [1, 1]
        for i in range(2, n + 1):
            one, two = two, one + two
        return two

class Solution1:
    def climbStairs(self, n: int) -> int:
        steps = [1, 1]
        if n < 2:
            return steps[n]
        for i in range(2, n + 1):
            steps.append(steps[i - 1] + steps[i - 2])
        return steps[-1]

        
