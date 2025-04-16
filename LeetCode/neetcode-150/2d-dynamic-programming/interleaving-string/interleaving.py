class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def backtrack(k, i, j):
            if k == len(s3):
                return True
            if i != len(s1) and j != len(s2):
                if s1[i] == s3[k] and backtrack(k + 1, i + 1, j):
                    return True
                if s2[j] == s3[k] and backtrack(k + 1, i, j + 1):
                    return True
                return False
            elif i == len(s1):
                if s2[j] == s3[k]:
                    return backtrack(k + 1, i, j + 1)
                else:
                    return False
            elif j == len(s2):
                if s1[i] == s3[k]:
                    return backtrack(k + 1, i + 1, j)
                else:
                    return False        

        if len(s1) + len(s2) != len(s3):
            return False
        return backtrack(0, 0, 0)
