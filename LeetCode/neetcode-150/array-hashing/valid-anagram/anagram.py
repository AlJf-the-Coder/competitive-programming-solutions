class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        if len(s_dict) != len(t_dict):
            return False
        for char in s_dict:
            if s_dict[char] != t_dict.get(char, 0):
                return False
        return True

    def isAnagramArr(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        s_dict = dict.fromkeys(letters, 0)
        t_dict = dict.fromkeys(letters, 0)
        for char in s:
            s_dict[char] += 1
        for char in t:
            t_dict[char] += 1
        for char in s_dict:
            if s_dict[char] != t_dict[char]:
                return False
        return True
