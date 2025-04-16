class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (n >> i) & 1:
                res |= 1 << (31 - i)
        return res

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            if (1 << i) & n:
                res += 1 << (31 - i)
        return res

class Solution1:
    def reverseBits(self, n: int) -> int:
        res = 0
        mask = 1 << 31
        add = 1
        for i in range(31, -1, -1):
            if mask & n:
                res += add
            mask >>= 1
            add <<= 1
        return res
