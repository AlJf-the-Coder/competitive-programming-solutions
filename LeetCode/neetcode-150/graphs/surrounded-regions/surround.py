class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(i, j):
            q = deque([(i, j)])
            while q:
                i, j = q.popleft()
                for di, dj in dirs:
                    row, col = i + di, j + dj
                    if min(row, col) < 0 or row == ROWS or col == COLS:
                        continue
                    if board[row][col] ==  'O':
                        q.append((row, col))
                        board[row][col] = 'Z'
        
        for i in range(ROWS):
            if board[i][0] == 'O':
                board[i][0] = 'Z'
                bfs(i, 0)
            if board[i][COLS - 1] == 'O':
                board[i][COLS - 1] = 'Z'
                bfs(i, COLS - 1)


        for j in range(COLS):
            if board[0][j] == 'O':
                board[0][j] = 'Z'
                bfs(0, j)
            if board[ROWS - 1][j] == 'O':
                board[ROWS - 1][j] = 'Z'
                bfs(ROWS - 1, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

class Solution1:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        skip = [[False] * COLS for i in range(ROWS)]
        def bfs(i, j):
            seen = {(i, j)}
            q = deque([(i, j)])
            skip[i][j] = True
            surrounded = True
            while q:
                i, j = q.popleft()
                for di, dj in dirs:
                    row, col = i + di, j + dj
                    if min(row, col) < 0 or row == ROWS or col == COLS:
                        surrounded = False
                        continue
                    if board[row][col] ==  'O' and (row, col) not in seen:
                        q.append((row, col))
                        seen.add((row, col))

            if surrounded:
                for i, j in seen:
                    board[i][j] = 'X'
            return
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and not skip[i][j]:
                    bfs(i, j)

