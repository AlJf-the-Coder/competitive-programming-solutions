class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {'}': '{', ']': '[', ')': '('}
        for char in s:
            if char in '[{(':
                stack.append(char)
            else:
                if stack == []:
                    return False
                popped = stack.pop()
                if popped != pairs[char]:
                    return False
        return stack == []

        
