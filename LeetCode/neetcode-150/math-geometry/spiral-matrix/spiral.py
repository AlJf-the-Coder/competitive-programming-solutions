class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ind = 0
        m, n = len(matrix), len(matrix[0])
        spiral = [None] * (n * m)
        for i in range(min(m,n) // 2):
            for j in range(i, n - 1 - i):
                spiral[ind] = matrix[i][j]
                ind += 1
            for j in range(i, m - 1 - i):
                spiral[ind] = matrix[j][n - 1 - i]
                ind += 1
            for j in range(n - 1 - i, i, -1):
                spiral[ind] = matrix[m - 1 - i][j]
                ind += 1
            for j in range(m - i - 1, i, -1):
                spiral[ind] = matrix[j][i]
                ind += 1
        if min(m, n) % 2 == 1:
            i = min(m, n) // 2
            for j in range(i, max(m, n) - i):
                spiral[ind] = matrix[i][j] if m <= n else matrix[j][i]
                ind += 1
        return spiral

