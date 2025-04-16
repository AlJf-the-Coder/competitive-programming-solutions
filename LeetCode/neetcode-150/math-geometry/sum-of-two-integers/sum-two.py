class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        res = 0
        i = 0
        while i < 12:
            a_bit = (a & 1)
            b_bit = (b & 1)
            res |= (a_bit ^ b_bit ^ c) << i
            c = a_bit & b_bit | a_bit & c | b_bit & c
            a >>= 1
            b >>= 1
            i += 1
        if (res >> (i - 1)) & 1:
            res |= -1 << i
        return res
