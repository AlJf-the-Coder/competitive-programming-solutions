class PriorityQueue:
    def __init__(self, cells):
        self.indices = {cell: i for cell, i in zip(cells, range(1, len(cells) + 1))}
        self.priorities = {cell: float("inf") for cell in cells}
        self.queue = [None] + cells
        self.queue_len = len(cells)

    def sift_up(self, i):
        p = i // 2
        if p > 0:
            if self.priorities[self.queue[i]] < self.priorities[self.queue[p]]:
                self.indices[self.queue[i]], self.indices[self.queue[p]] = p, i
                self.queue[i], self.queue[p] = self.queue[p], self.queue[i]
                self.sift_up(p)

    def sift_down(self, i):
        l = 2 * i
        r = 2 * i + 1
        s = i
        if l <= self.queue_len and self.priorities[self.queue[s]] > self.priorities[self.queue[l]]:
            s = l
        if r <= self.queue_len and self.priorities[self.queue[s]] > self.priorities[self.queue[r]]:
            s = r
        if s != i:
            self.indices[self.queue[i]], self.indices[self.queue[s]] = s, i
            self.queue[i], self.queue[s] = self.queue[s], self.queue[i]
            self.sift_down(s)

    def update_priority(self, node, prio):
        self.priorities[node] = prio
        self.sift_up(self.indices[node])

    def pop(self):
        item = self.queue[1]
        self.queue[1] = self.queue[self.queue_len]
        self.indices[self.queue[1]] = 1
        self.queue_len -= 1
        self.sift_down(1)
        return self.priorities[item], item
    
    def is_empty(self):
        return self.queue_len == 0


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        cells = []
        adj_list = defaultdict(list)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                cells.append((i, j))
                if i - 1 >= 0:
                    adj_list[(i, j)].append((i - 1, j))
                if i + 1 < n:
                    adj_list[(i, j)].append((i + 1, j))
                if j - 1 >= 0:
                    adj_list[(i, j)].append((i, j - 1))
                if j + 1 < n:
                    adj_list[(i, j)].append((i, j + 1))

        max_seen = 0
        visited = set()
        pq = PriorityQueue(cells)
        pq.update_priority((0, 0), 0)
        while not pq.is_empty():
            weight, node = pq.pop()
            i, j = node
            max_seen = max(max_seen, grid[i][j])
            if node == (n - 1, n - 1):
                break
            visited.add(node)
            for nei in adj_list[node]:
                if nei in visited:
                    continue
                i, j = nei
                pq.update_priority(nei, grid[i][j])

        return max_seen

