class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(q, fresh):
            time = 0
            while fresh > 0 and q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if min(ni, nj) < 0 or ni == m or nj == n or grid[ni][nj] != 1:
                            continue
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))
                time += 1
            return time if not fresh else -1

        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        return bfs(q, fresh)
        
        
class Solution1:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        all_empty = all(all(map(lambda o: o == 0, grid[i])) for i in range(m))
        if all_empty:
            return 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def rot(i, j):
            if grid[i][j] == 2:
                grid[i][j] = 0
                for di, dj in dirs:
                    new_i = i + di
                    new_j = j + dj
                    if new_i < 0 or new_i > m - 1 or new_j < 0 or new_j > n - 1:
                        continue
                    if grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = -1
        time = 0
        all_rotten = all(all(map(lambda o: o != 1, grid[i])) for i in range(m))
        all_fresh = all(all(map(lambda o: o != 2, grid[i])) for i in range(m))
        while not all_rotten and not all_fresh:
            for i in range(m):
                for j in range(n):
                    rot(i, j)
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == -1:
                        grid[i][j] = 2
            time += 1
            all_rotten = all(all(map(lambda o: o == 2 or o == 0, grid[i])) for i in range(m))
            all_fresh = all(all(map(lambda o: o == 1 or o == 0, grid[i])) for i in range(m))
        return time if not all_fresh else -1
