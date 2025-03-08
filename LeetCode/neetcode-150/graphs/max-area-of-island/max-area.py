class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                char = grid[i][j]
                if char != 1:
                    continue
                island_area = 0
                q = deque([(i, j)])
                grid[i][j] = -1
                while q:
                    i, j = q.popleft()
                    island_area += 1
                    for di, dj in dirs:
                        n_i, n_j = i + di, j + dj
                        if n_i < 0 or n_i > m - 1 or n_j < 0 or n_j > n - 1 or grid[n_i][n_j] != 1:
                            continue
                        grid[n_i][n_j] = -1
                        q.append((n_i, n_j))
                max_area = max(max_area, island_area)
        return max_area

class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or grid[i][j] != 1:
                return 0
            area = 1
            grid[i][j] = -1
            for di, dj in dirs:
                area += dfs(i + di, j + dj)
            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                max_area = max(max_area, dfs(i, j))
        return max_area
