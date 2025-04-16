class Trie:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True

class Trie1:

    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            ind = ord(c) - 97
            if not cur.children[ind]:
                cur.children[ind] = Trie()
            cur = cur.children[ind]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            ind = ord(c) - 97
            if cur.children[ind]:
                cur = cur.children[ind]
            else:
                return False
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            ind = ord(c) - 97
            if cur.children[ind]:
                cur = cur.children[ind]
            else:
                return False
        return True
