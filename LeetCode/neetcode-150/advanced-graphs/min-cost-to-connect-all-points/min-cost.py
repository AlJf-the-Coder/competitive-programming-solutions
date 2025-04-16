class PriorityQueue:
    def __init__(self, points):
        self.indices = {point: i for point, i in  zip(points, range(1, len(points) + 1))}
        self.priorities = {point: float("inf") for point in points}
        self.queue = [None] + points.copy()
        self.queue_len = len(points)

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
    def manhattan(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = list(map(tuple, points))
        frontier = set(points)
        cost = 0
        pq = PriorityQueue(points)
        start = frontier.pop()
        pq.update_priority(start, 0)
        frontier.add(start)
        while not pq.is_empty():
            weight, point = pq.pop()
            cost += weight
            frontier.remove(point)
            for nei in frontier:
                pq.update_priority(nei, min(pq.priorities[nei], self.manhattan(point, nei)))

        return cost

class DSU:
    def __init__(self, points):
        self.parents = [-1] * len(points)
        self.indices = {point: i for point, i in zip(points, range(len(points)))}
        
    def find(self, i):
        if self.parents[i] < 0:
            return i
        p = self.parents[i]
        self.parents[i] = self.find(p)
        return self.parents[i]

    def union(self, p1, p2):
        pr1 = self.find(self.indices[p1])
        pr2 = self.find(self.indices[p2])
        if pr1 == pr2:
            return False
        if self.parents[pr1] < self.parents[pr2]:
            self.parents[pr1] += self.parents[pr2]
            self.parents[pr2] = pr1
        else:
            self.parents[pr2] += self.parents[pr1]
            self.parents[pr1] = pr2
        return True


class Solution1:
    def manhattan(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = list(map(tuple, points))
        dsu = DSU(points)
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                pi, pj = points[i], points[j]
                edges.append([self.manhattan(pi, pj), pi, pj])
        edge_count = 0
        heapify(edges)
        cost = 0
        while edge_count != len(points) - 1:
            weight, pi, pj = heappop(edges)
            if dsu.union(pi, pj):
                cost += weight
                edge_count += 1

        return cost
