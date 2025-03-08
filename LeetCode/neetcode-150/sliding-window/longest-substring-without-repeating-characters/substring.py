class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win_size = 0
        l = 0
        n = len(s)
        chars = dict()
        for r in range(n):
            if s[r] in chars:
                l = max(chars[s[r]] + 1, l)
            chars[s[r]] = r
            win_size = max(win_size, r - l + 1)
        return win_size

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win_size = 0
        n = len(s)
        l, r = 0, 1
        chars = set(s[0]) if s else set()
        while r < n:
            cur = s[r]
            if cur not in chars:
                chars.add(cur)
                r += 1
            else:
                win_size = max(win_size, r - l)
                while s[l] != cur:
                    chars.remove(s[l])
                    l += 1
                chars.remove(s[l])
                l += 1
        win_size = max(win_size, n - l)
        return win_size

from collections import OrderedDict
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win_size = 0
        i, n = 0, len(s)
        chars = OrderedDict()
        char_count = 0
        while i < n:
            cur = s[i]
            if cur not in chars:
                chars[cur] = i
                char_count += 1
                if char_count == win_size + 1:
                    win_size += 1
            else:
                char, i = chars.popitem(last=False)
                char_count -= 1
                while char != cur:
                    char, i = chars.popitem(last=False)
                    char_count -= 1
                i = i + char_count
            i += 1
        return win_size
