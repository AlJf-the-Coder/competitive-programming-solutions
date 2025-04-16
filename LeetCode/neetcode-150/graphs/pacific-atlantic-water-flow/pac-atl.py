class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j, pac):
            seen = pacific if pac else atlantic
            if (i, j) in seen:
                return
            seen.add((i, j))
            for di, dj in dirs:
                row, col = i + di, j + dj
                if min(row, col) < 0 or row == ROWS or col == COLS:
                    continue
                if heights[row][col] >= heights[i][j]:
                    dfs(row, col, pac)

        for i in range(ROWS):
            dfs(i, 0, True)
            dfs(i, COLS - 1, False)

        for j in range(COLS):
            dfs(0, j, True)
            dfs(ROWS - 1, j, False)

        return list(pacific & atlantic)
