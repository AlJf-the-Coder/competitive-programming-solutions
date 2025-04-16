class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        powers = set()
        p = 1
        while p <= n:
            powers.add(p)
            p <<= 1
        '''

        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            #if i in powers:
            if i == offset * 2:
                offset = i
            dp[i] = dp[i - offset] + 1
        return dp

class Solution1:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        ones = 0
        for i in range(1, n + 1):
            while i & 1 == 0:
                i >>= 1
                ones -= 1
            ones += 1
            res.append(ones)
        return res
