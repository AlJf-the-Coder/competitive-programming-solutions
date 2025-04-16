class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_a = 0
        p_b = len(s) - 1
        while p_a <= p_b:
            while p_a < len(s) and not s[p_a].isalnum():
                p_a += 1
            while p_b >= 0 and not s[p_b].isalnum():
                p_b -= 1
            if p_a < len(s) and p_b >= 0 and s[p_a].lower() != s[p_b].lower():
                return False
            p_a += 1
            p_b -= 1
        return True
        
