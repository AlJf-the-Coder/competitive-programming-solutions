class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n > 0:
            n &= (n - 1)
            weight += 1
        return weight

class Solution1:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n > 0:
            weight += 1 & n
            n >>= 1
        return weight

class Solution2:
    def hammingWeight(self, n: int) -> int:
        n_bits = math.floor(math.log2(n))
        weight = 0
        for i in range(n_bits + 1):
            if (1 << i) & n:
                weight += 1
        return weight
