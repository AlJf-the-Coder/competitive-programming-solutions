class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_word = False


    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = WordDictionary()
            cur = cur.children[c]
        cur.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(j, trie):
            cur = trie
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                elif c in cur.children:
                    cur = cur.children[c]
                else:
                    return False
            return cur.is_word
        return dfs(0, self)

    def search1(self, word: str) -> bool:
        cur = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for w in cur.children:
                    tmp = cur
                    cur = cur.children[w]
                    if cur.search(word[i + 1:]):
                        return True
                    cur = tmp
                return False
            elif c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.is_word
