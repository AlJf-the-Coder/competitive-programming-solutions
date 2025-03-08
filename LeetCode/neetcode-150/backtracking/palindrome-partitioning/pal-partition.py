class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        parts = []
        part = []

        @cache
        def is_palindrome(l, r):
            if r <= l:
                return True
            return s[l] == s[r] and is_palindrome(l + 1, r - 1)

        def divide(j, i):
            if j > n - 1:
                parts.append(part.copy())
                return
            if is_palindrome(j, i):
                part.append(s[j: i + 1])
                divide(i + 1, i + 1)
                part.pop()
            if i < n - 1:
                divide(j, i + 1)
        divide(0, 0)
            
        return parts

class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        parts = []
        part = []

        def divide(i, string):
            if i == d:
                if not string:
                    parts.append(part.copy())
                return
            for j in range(0, len(string)):
                substr = string[: j + 1]
                if self.is_palindrome(substr):
                    part.append(substr)
                    divide(i + 1, string[j + 1: ])
                    part.pop()


        for d in range(1, n + 1):
            divide(0, s)
            
        return parts

    @cache
    def is_palindrome(self, s):
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
