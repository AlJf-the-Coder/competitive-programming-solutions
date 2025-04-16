class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        greater = [[[] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                    if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                        greater[i][j].append((i - 1, j))
                    if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
                        greater[i][j].append((i + 1, j))
                    if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                        greater[i][j].append((i, j - 1))
                    if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
                        greater[i][j].append((i, j + 1))

        prev = [[True] * n for i in range(m)]
        for k in range(m * n):
            cur = [[False] * n for i in range(m)]
            has_path = False
            for i in range(m):
                for j in range(n):
                    if not prev[i][j]:
                        continue
                    for n_i, n_j in greater[i][j]:
                        if not cur[n_i][n_j]:
                            cur[n_i][n_j] = True
                            if not has_path:
                                has_path = True                            
            if not has_path:
                break
            prev = cur       
        return k + 1

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prev = [[True] * n for i in range(m)]
        for k in range(m * n):
            cur = [[False] * n for i in range(m)]
            has_path = False
            for i in range(m):
                for j in range(n):
                    if not prev[i][j]:
                        continue
                    if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j] and not cur[i - 1][j]:
                        cur[i - 1][j] = True
                        has_path = True
                    if i + 1 < m and matrix[i + 1][j] > matrix[i][j] and not cur[i + 1][j]:
                        cur[i + 1][j] = True
                        has_path = True
                    if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j] and not cur[i][j - 1]:
                        cur[i][j - 1] = True  
                        has_path = True           
                    if j + 1 < n and matrix[i][j + 1] > matrix[i][j] and not cur[i][j + 1]:
                        cur[i][j + 1] = True
                        has_path = True
            if not has_path:
                break
            prev = cur       
        return k + 1

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                q.append((i, j))
        length = 0
        while q:
            length += 1
            visit = set()
            for i in range(len(q)):
                i, j = q.popleft()
                if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j] and (i - 1, j) not in visit:
                    q.append((i - 1, j))
                    visit.add((i - 1, j))
                if i + 1 < m and matrix[i + 1][j] > matrix[i][j] and (i + 1, j) not in visit:
                    q.append((i + 1, j))
                    visit.add((i + 1, j))
                if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j] and (i, j - 1) not in visit:
                    q.append((i, j - 1))
                    visit.add((i, j - 1))                    
                if j + 1 < n and matrix[i][j + 1] > matrix[i][j] and (i, j + 1) not in visit:
                    q.append((i, j + 1))
                    visit.add((i, j + 1))                    
        return length

