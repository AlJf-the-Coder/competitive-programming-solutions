class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        cols = [False] * n
        rows = [False] * m
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols[j] = True
                    rows[i] = True

        for i in range(m):
            if rows[i]:
                for k in range(n):
                    matrix[i][k] = 0

        for j in range(n):
            if cols[j]:
                for k in range(m):
                    matrix[k][j] = 0                    

