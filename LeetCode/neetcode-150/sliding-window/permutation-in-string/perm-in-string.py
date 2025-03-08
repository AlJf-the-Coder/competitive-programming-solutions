from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2: 
            return False
        s1_counts = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
        cur_counts = dict(s1_counts)
        for c in s1:
            s1_counts[c] += 1
        for i in range(n1):
            cur_counts[s2[i]] += 1
        if cur_counts == s1_counts:
            return True
        for r in range(n1, n2):
            cur_counts[s2[r - n1]] -= 1
            cur_counts[s2[r]] += 1
            if cur_counts == s1_counts:
                return True
        return False

class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2: 
            return False
        s1_counts = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
        cur_counts = dict(s1_counts)
        for c in s1:
            s1_counts[c] += 1
        for i in range(n1):
            cur_counts[s2[i]] += 1
        matches = 0
        for c in s1_counts:
            if s1_counts[c] == cur_counts[c]:
                matches += 1
        for r in range(n1, n2):
            if matches == 26:
                return True
            c = s2[r - n1]
            cur_counts[c] -= 1
            if s1_counts[c] == cur_counts[c]:
                matches += 1
            elif s1_counts[c] - 1 == cur_counts[c]:
                matches -= 1
            
            c = s2[r]
            cur_counts[c] += 1
            if s1_counts[c] == cur_counts[c]:
                matches += 1
            elif s1_counts[c] + 1 == cur_counts[c]:
                matches -= 1
            
        return matches == 26

class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        n1 = len(s1)
        n2 = len(s2)
        cur_counts = Counter(s2[:n1])
        if cur_counts == s1_counts:
                return True
        for r in range(n1, n2):
            cur_counts[s2[r - n1]] -= 1
            cur_counts[s2[r]] += 1
            if cur_counts == s1_counts:
                return True
        return False

from collections import defaultdict
class Solution3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = defaultdict(int)
        n1 = 0
        for c in s1:
            s1_counts[c] += 1
            n1 += 1
        cur_counts = defaultdict(int)
        i = 0
        n2 = len(s2)
        while i <= n2 - n1:
            cur_counts.clear()
            j = i
            while j < i + n1:
                if s2[j] in s1_counts:
                    cur_counts[s2[j]] += 1
                    j += 1
                else:
                    i = j + 1
                    break
            else:
                if cur_counts == s1_counts:
                    return True
                i += 1
        return False

