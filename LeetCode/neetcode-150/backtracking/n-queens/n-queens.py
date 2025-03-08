class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = [['.'] * n for i in range(n)]

        def dfs(i):
            if i == n:
                res.append(["".join(row) for row in board])
            for j in range(n):
                if j in cols or (i - j) in pos_diag or (i + j) in neg_diag:
                    continue
                cols.add(j)
                pos_diag.add(i - j)
                neg_diag.add(i + j)
                board[i][j] = 'Q'
                dfs(i + 1)
                board[i][j] = '.'
                neg_diag.remove(i + j)
                pos_diag.remove(i - j)
                cols.remove(j)
        dfs(0)
        return res

class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        indices = set()
        col_inds = [-1] * n

        def is_attacking(i, j):
            for r in range(max(i - j, 0), i):
                if col_inds[r] == j - (i - r) or col_inds[r] == j + (i - r):
                    return True
            for r in range(max(i - n + j + 1, 0), i):
                if col_inds[r] == j - (i - r) or col_inds[r] == j + (i - r):
                    return True
            return False


        def dfs(i):
            if i == n:
                res.append(["".join("Q" if c == j else '.' for c in range(n)) for j in col_inds])
            for j in range(n):
                if j not in indices and not is_attacking(i, j):
                    indices.add(j)
                    col_inds[i] = j
                    dfs(i + 1)
                    indices.remove(j)
        dfs(0)
        return res

   


            
