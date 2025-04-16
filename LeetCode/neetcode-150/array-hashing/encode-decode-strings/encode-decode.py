class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for string in strs:
            encoding += f"{len(string)}#{string}"
        return encoding

    def decode(self, s: str) -> List[str]:
        length = ""
        strs = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '#':
                m = int(length)
                length = ""
                strs.append(s[i + 1: i + m + 1])
                i += m + 1
            else:
                length += s[i]
                i += 1

        return strs

class Solution1:

    encodings = {}
    decodings = {}
    def encode(self, strs: list) -> str:
        self.encodings.clear()
        self.decodings.clear()
        ind = 0
        encodings = []
        for string in strs:
            if string not in self.encodings:
                s_ind = str(ind)
                self.encodings[string] = s_ind
                encodings.append(s_ind)
                self.decodings[s_ind] = string
                ind += 1
            else:
                encodings.append(self.encodings[string])

        return ' '.join(encodings)
        '''
        if strs == [""]: return chr(0)
        return chr(0).join(strs)
        '''

    def decode(self, s: str) -> list:
        return [self.decodings[encoding] for encoding in s.split()]


