class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        l, r = 0, x + 1
        while l < r:
            mid = (l + r) // 2
            if mid * mid < x:
                res = mid
                l = mid + 1
            elif mid * mid > x:
                r = mid
            else:
                return mid
        return res
