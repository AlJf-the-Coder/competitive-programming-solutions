class Solution:
    # O(len(t)) space
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            temp = dp[0]
            for j in range(1, min(i + 1, len(t) + 1)):
                if s[i - 1] == t[j - 1]:
                    dp[j], temp = temp + dp[j], dp[j]
                else:
                    temp = dp[j]
        return dp[len(t)]

class Solution:
    # O(len(s)) space
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] * (len(s) + 1)
        for i in range(1, len(t) + 1):
            temp = dp[i - 1]
            dp[i - 1] = 0
            for j in range(i, len(s) + 1):
                temp2 = dp[j]
                dp[j] = dp[j - 1]
                if s[j - 1] == t[i - 1]:
                    dp[j] += temp
                temp = temp2
        return dp[len(s)]

class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for i in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dp[0][i] = 1
        for i in range(1, len(t) + 1):
            for j in range(i, len(s) + 1):
                dp[i][j] += dp[i][j - 1]
                if s[j - 1] == t[i - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[len(t)][len(s)]

