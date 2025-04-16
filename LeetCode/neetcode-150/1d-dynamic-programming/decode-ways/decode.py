class Solution:
    def numDecodings(self, s: str) -> int:
        keys = {str(i) for i in range(1, 27)}
        n = len(s)
        ways = [0] * n
        if s[0] == '0':
            return 0
        ways[0] = 1
        if n == 1:
            return ways[0]
        if s[0: 2] in keys:
            ways[1] += 1
        if s[1] != '0':
            ways[1] += 1
        for i in range(2, n):
            if s[i - 1: i + 1] in keys:
                ways[i] += ways[i - 2]
            if s[i] != '0':
                ways[i] += ways[i - 1]
        return ways[n - 1]

class Solution1:
    def numDecodings(self, s: str) -> int:
        keys = {str(i) for i in range(1, 27)}
        n = len(s)
        ways = [0] * n
        if s[0] == '0':
            return 0
        ways[0] = 1
        if n == 1:
            return ways[0]
        if s[0:2] == '00':
            return 0
        if s[0:2] in ['10', '20']:
            ways[1] = 1
        elif s[0:2] in keys:
            ways[1] = 2
        elif s[1] != '0':
            ways[1] = ways[0]
        else:
            return 0
        for i in range(2, n):
            if s[i - 1: i + 1] == '00':
                return 0
            if s[i - 1: i + 1] in ['10', '20']:
                ways[i] = ways[i - 2]
            elif s[i - 1: i + 1] in keys:
                ways[i] = ways[i - 1] + ways[i - 2]
            elif s[i] != '0':
                ways[i] = ways[i - 1]
            else:
                return 0
        return ways[n - 1]
