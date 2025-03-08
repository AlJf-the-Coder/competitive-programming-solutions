class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = (1 << 31) - 1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(q):
            level = 1
            while q:
                print(grid)
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for d_i, d_j in dirs:
                        ni, nj = i + d_i, j + d_j
                        if min(ni, nj) < 0 or ni == ROWS or nj == COLS or \
                    grid[ni][nj] != INF:
                            continue
                        grid[ni][nj] = level
                        q.append((ni, nj))
                level += 1
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if not grid[i][j]:
                    q.append((i, j))
        bfs(q)

class Solution1:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(i, j):
            q = deque([(i, j, 0)])
            while q:
                i, j, dist = q.popleft()
                if i < 0 or i >= ROWS or j < 0 or j >= COLS or \
                grid[i][j] < 0 or dist > grid[i][j]:
                    continue
                grid[i][j] = dist
                for d_i, d_j in dirs:
                    q.append((i + d_i, j + d_j, dist + 1))

        for i in range(ROWS):
            for j in range(COLS):
                if not grid[i][j]:
                    bfs(i, j)

class Solution2:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, dist):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or \
              grid[i][j] < 0 or dist > grid[i][j]:
                return
            grid[i][j] = dist
            for d_i, d_j in dirs:
                dfs(i + d_i, j + d_j, dist + 1)

        for i in range(ROWS):
            for j in range(COLS):
                if not grid[i][j]:
                    dfs(i, j, 0)
