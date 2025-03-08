from collections import Counter

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counter = defaultdict(int)
        max_len = 0
        max_f = 0
        l = 0
        for r in range(n):
            counter[s[r]] += 1
            max_f = max(max_f, counter[s[r]])
            width = r - l + 1
            if width - max_f <= k:
                max_len = max(max_len, width)
            else:
                counter[s[l]] -= 1
                l += 1          
        return max_len

class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        min_width = self.longest_repeating(s, n)
        if n - min_width <= k:
            return n
        max_len = min_width + k

        for w in range(min_width + k + 1, n + 1):
            update = False
            counter = Counter(s[: w])
            last_ind = n - w
            for i in range(last_ind + 1):
                common_count = counter.most_common(1)[0][1]
                if w - common_count <= k:
                    max_len = w
                    update = True
                    break
                if i < last_ind:
                    counter[s[i]] -= 1
                    counter[s[i + w]] += 1
            if not update:
                break
        return max_len

    def longest_repeating(self, s, n):
        max_len = 0
        c_len = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                c_len += 1
            else:
                max_len = max(c_len, max_len)
                c_len = 1
        return max_len

class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            for j in range(i, n):
                counter = Counter(s[i:j + 1])
                width = j - i + 1
                common_count = counter.most_common(1)[0][1]
                if common_count + min(k, width - common_count) == width:
                    max_len = max(max_len, width)
        return max_len

