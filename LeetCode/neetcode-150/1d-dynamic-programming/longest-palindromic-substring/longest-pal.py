class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        p = -1
        p_len = 0
        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r <= n and s[l] == s[r - 1]:
                if r - l > p_len:
                    p = l
                    p_len = r - l
                l -= 1
                r += 1
            l, r = i, i + 2
            while l >= 0 and r <= n and s[l] == s[r - 1]:
                if r - l > p_len:
                    p = l
                    p_len = r - l
                l -= 1
                r += 1
        return s[p: p + p_len]
