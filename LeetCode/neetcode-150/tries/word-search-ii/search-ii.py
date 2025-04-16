class Trie:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.seen = False
        self.counts = 0

    def insert(self, word: str) -> None:
        cur = self
        cur.counts += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
            cur.counts += 1
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        seen = []
        def search(i, j, word, trie):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or trie.counts == 0 or board[i][j] not in trie.children:
                return 0
            counts = 0
            word += board[i][j]
            par = trie
            trie = trie.children[board[i][j]]
            if trie.is_word and not trie.seen:
                seen.append(word)
                trie.seen = True
                counts += 1
                trie.counts -= 1
            temp = board[i][j]
            board[i][j] = '#'
            counts += search(i - 1, j, word, trie) + search(i + 1, j, word, trie) +\
                     search(i, j - 1, word, trie) + search(i, j + 1, word, trie)
            par.counts -= counts
            board[i][j] = temp
            return counts

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    search(i, j, '', trie)

        return seen

class Trie:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.seen = False

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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        seen = []
        def search(i, j, word, trie):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or board[i][j] not in trie.children:
                return
            word += board[i][j]
            trie = trie.children[board[i][j]]
            if trie.is_word and not trie.seen:
                seen.append(word)
                trie.seen = True
            temp = board[i][j]
            board[i][j] = '#'
            search(i - 1, j, word, trie)
            search(i + 1, j, word, trie)
            search(i, j - 1, word, trie)
            search(i, j + 1, word, trie)
            board[i][j] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    search(i, j, '', trie)

        return seen
