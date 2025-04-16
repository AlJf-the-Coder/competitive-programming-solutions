class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counts = Counter(magazine)
        ran_counts = Counter(ransomNote)
        return ran_counts <= mag_counts

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counts = Counter(magazine)
        ran_counts = Counter(ransomNote)
        for c in ran_counts:
            if mag_counts[c] < ran_counts[c]:
                return False
        return True
