class Solution:
    def myPow(self, x: float, n: int) -> float:
        stack = []
        res = 1
        neg = n < 0
        n = abs(n)
        while n != 0:
            stack.append(n)
            if n % 2 == 1:
                n = n - 1
            else:
                n //= 2
        while stack:
            if stack.pop() % 2 == 1:
                res *= x
            else:
                res *= res

        if neg:
            return 1 / res
        return res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def help(n):
            if n == 0:
                return 1
            if n % 2 == 0:
                half = help(n // 2)
                return half * half
            else:
                return x * help(n - 1)
        if n < 0:
            return 1 / help(-n)
        return help(n)
