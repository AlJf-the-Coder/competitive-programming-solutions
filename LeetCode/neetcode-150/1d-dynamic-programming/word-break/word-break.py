class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lengths = defaultdict(list)
        for word in wordDict:
            lengths[len(word)].append(word)        
        in_dict = [False] * (len(s) + 1)
        in_dict[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            substr = s[i:]
            for length in range(1, 21):
                if length + i > len(s):
                    break
                if not in_dict[i + length]:
                    continue
                for word in lengths[length]:
                    if substr.startswith(word):
                        in_dict[i] = True
                        break
                if in_dict[i]:
                    break                      
        return in_dict[0]

class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.is_word = True
    
    def find(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        t = 0
        for word in wordDict:
            trie.insert(word)
            t = max(t, len(word))
        in_dict = [False] * (len(s) + 1)
        in_dict[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, min(i + t, len(s))):
                if not in_dict[j + 1]:
                    continue
                is_word = trie.find(s[i: j + 1])
                if is_word == None:
                    break
                if is_word:
                    in_dict[i] = True
                    break                   
        return in_dict[0]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        in_dict = [False] * (len(s) + 1)
        in_dict[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):
                if s[i:j + 1] in wordDict and in_dict[j + 1]:
                    in_dict[i] = True
                    break          
        return in_dict[0]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        @cache
        def recurse(i, j):
            if i == j == len(s):
                return True
            if j == len(s):
                return False
            if s[i: j + 1] in wordDict and recurse(j + 1, j + 1):
                return True
            return recurse(i, j + 1)
        return recurse(0, 0)

