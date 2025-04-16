from collections import deque, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freq_t, freq_s = defaultdict(int), defaultdict(int)
        m = len(s)
        n = len(t)
        for r in range(n):
            freq_t[t[r]] += 1

        need = n
        have = 0
        l = 0
        min_len = m + 1
        res = [-1, -1]
        for r in range(m):
            freq_s[s[r]] += 1
            if freq_s[s[r]] <= freq_t[s[r]]:
                have += 1
            if have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res =  [l, r]
                while have == need:
                    freq_s[s[l]] -= 1
                    if freq_s[s[l]] < freq_t[s[l]]:
                        if r - l + 1 < min_len:
                            min_len = r - l + 1
                            res =  [l, r]
                        have -= 1
                    l += 1                
        l, r = res
        return s[l: r + 1] if min_len < m + 1 else ""

class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        
        freq_t = dict.fromkeys([chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)], 0)
        freq_s = dict(freq_t)
        m = len(s)
        n = len(t)
        for r in range(n):
            freq_t[t[r]] += 1 

        matches = 0
        for count in freq_t.values():
            if not count:
                matches += 1

        l = 0
        min_len = m + 1
        res = ""
        win = deque()
        for r in range(m):
            win.append(s[r])
            freq_s[s[r]] += 1
            if freq_s[s[r]] == freq_t[s[r]]:
                matches += 1
            if matches == 52:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res =  "".join(win)
                while l <= r:
                    freq_s[s[l]] -= 1
                    if freq_s[s[l]] < freq_t[s[l]]:
                        if r - l + 1 < min_len:
                            min_len = r - l + 1
                            res =  "".join(win)
                        matches -= 1
                        win.popleft()
                        l += 1
                        break
                    win.popleft()
                    l += 1                

        return res
