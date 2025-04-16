class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2, = text2, text1
        n, m = len(text1), len(text2)
        row = [0] * (m + 1)
        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                temp = row[j]
                if text1[i - 1] == text2[j - 1]:
                    row[j] = 1 + prev
                else:
                    row[j] = max(row[j], row[j - 1])
                prev = temp
        return row[m]

class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        row = [0] * (n + 1)
        for i in range(1, m + 1):
            new_row = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    new_row[j] = 1 + row[j - 1]
                else:
                    new_row[j] = max(row[j], new_row[j - 1])
            row = new_row
        return row[n]

class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def recurse(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + recurse(i + 1, j + 1)
            else:
                return max(recurse(i, j + 1), recurse(i + 1, j))
        return recurse(0, 0)
