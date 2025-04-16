class PriorityQueue:
    def __init__(self, n, start):
        self.indices = list(range(n + 1))
        self.priorities = [float("inf")] * (n + 1)
        self.queue = list(range(n + 1))
        self.queue_len = n

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
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for i in range(n + 1)]
        for tup in times:
            src, trg, wei = tup
            adj_list[src].append((wei, trg))

        delays = [float("inf") for i in range(n + 1)]
        visited = [False] * (n + 1)
        pq = PriorityQueue(n, k)
        pq.update_priority(k, 0)
        while not pq.is_empty():
            weight, node = pq.pop()
            if weight == float("inf"):
                return -1
                
            delays[node] = weight
            visited[node] = True
            for wei, nei in adj_list[node]:
                if visited[nei]:
                    continue
                pq.update_priority(nei, min(pq.priorities[nei], delays[node] + wei))

        """
        max_delay = max(delays[1:])
        return max_delay if max_delay != float("inf") else -1
        """
        return max(delays[1:])

class Solution1:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delays = [float("inf")] * (n + 1)
        adj_list = [[] for i in range(n + 1)]
        for tup in times:
            src, trg, wei = tup
            adj_list[src].append((wei, trg))
        visited = [False] * (n + 1)
        addresses = [[float("inf"), i] for i in range(n + 1)]
        addresses[k][0] = 0
        
        pq = addresses.copy()
        heapq.heapify(pq)
        pq.remove([float("inf"), 0])
        while pq:
            weight, node = heappop(pq)
            if weight == float("inf"):
                return -1
            visited[node] = True
            delays[node] = weight
            for wei, nei in adj_list[node]:
                if visited[nei]:
                    continue
                addresses[nei][0] = min(addresses[nei][0], delays[node] + wei)
            heapq.heapify(pq)

        return max(delays[1:])
