class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return
            if grid[i][j] == '1':
                grid[i][j] = 'x'
                for di, dj in dirs:
                    dfs(i + di, j + dj)

        islands = 0
        for i in range(m):
            for j in range(n):
                char = grid[i][j]
                if char == '0' or char == 'x':
                    continue
                islands += 1
                dfs(i, j)
        return islands
