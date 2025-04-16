class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        star = []
        re_chars = []
        ind = 0
        i = 0
        while i < len(p):
            re_chars.append(p[i])
            if i + 1 < len(p) and p[i + 1] == '*':
                star.append(True)
                i += 1
            else:
                star.append(False)
            ind += 1
            i += 1

        dp_1 = [False] * (len(star) + 1)
        dp_2 = [False] * (len(star) + 1)

        dp_1[0] = True
        for i in range(1, len(star) + 1):
            if star[i - 1]:
                dp_1[i] = dp_1[i - 1]

        for i in range(len(s)):
            for j in range(1, len(star) + 1):
                dp_2[j] = False
                if re_chars[j - 1] == '.' or re_chars[j - 1] == s[i]:
                    dp_2[j] = dp_1[j - 1]
                    if not dp_2[j] and star[j - 1]:
                        dp_2[j] = dp_1[j]
                if not dp_2[j] and star[j - 1]:
                    dp_2[j] = dp_2[j - 1]
            dp_1, dp_2 = dp_2, dp_1
            dp_2[0] = False
        return dp_1[len(star)]
