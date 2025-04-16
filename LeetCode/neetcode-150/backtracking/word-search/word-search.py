class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        def search(word_i, i, j):
            if word_i == w:
                return True
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or board[i][j] != word[word_i]:
                return False
            board[i][j] = '#'
            found = search(word_i + 1, i - 1, j) or \
                search(word_i + 1, i + 1, j) or \
                search(word_i + 1, i, j - 1) or \
                search(word_i + 1, i, j + 1)
            board[i][j] = word[word_i]
            return found

        for i in range(m):
            for j in range(n):
                if search(0, i, j):
                    return True
        return False

class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        seen = [[False] * n for i in range(m)]
        def search(word_i, i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return False
            if board[i][j] == word[word_i] and not seen[i][j]:
                if word_i == w - 1:
                    return True
                seen[i][j] = True
                for di, dj in dirs:
                    if search(word_i + 1, i + di, j + dj):
                        return True
                seen[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if search(0, i, j):
                    return True
        return False
