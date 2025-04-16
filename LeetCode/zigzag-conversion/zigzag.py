class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)] 
        down = True
        r = 0
        for char in s:
            rows[r].append(char)
            if down:
                if r == numRows - 1:
                    down = False
                    r -= 1
                else:
                    r += 1
            else:
                if r == 0:
                    down = True 
                    r += 1
                else:
                    r -= 1
        '''
        for i, char in enumerate(s):
            ind = i % (2 * numRows - 2)
            if ind >= numRows:
                ind = numRows - (ind - numRows) - 2
            rows[ind].append(char)
        '''
        
        return ''.join(''.join(row) for row in rows)

    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        zigged = ""
        n_chars = len(s)
        c1, c2 = 2 * numRows - 2, 0
        for r in range(numRows):
            x = c1 if c1 != 0 else c2
            y = c2 if c2 != 0 else c1
            ind = r
            while ind < n_chars:
                zigged += s[ind]
                ind += x
            x, y = y, x
            c1 -= 2
            c2 += 2
        
        return zigged
