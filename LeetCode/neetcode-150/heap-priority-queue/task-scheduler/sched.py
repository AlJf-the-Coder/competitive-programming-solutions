import heapq
from collections import defaultdict
from typing import List

class Solution:    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        heap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(heap)

        intervals = 0
        while heap or queue:         
            if queue and queue[0][1] == intervals:
                c, _ = queue.popleft()
                heapq.heappush(heap, c)

            if heap:
                c = heapq.heappop(heap)
                c += 1
                if c != 0:
                    queue.append([c, intervals + n + 1])
            
            intervals += 1
        return intervals


class Solution1:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for t in tasks:
            counts[t] += 1
        task_delays = {}
        heap = []
        for t, c in counts.items():
            item = [0, -c, t]
            heap.append(item)
            task_delays[t] = item

        del counts
        heapq.heapify(heap)

        intervals = 0
        while heap:
            for t in task_delays:
                if task_delays[t][0] == 0:
                    continue
                task_delays[t][0] -= 1
            heapq.heapify(heap)

            if heap[0][0] == 0:
                _, _, top = heapq.heappop(heap)
                task_delays[top][0] = n + 1
                task_delays[top][1] += 1
                if task_delays[top][1] < 0:
                    heapq.heappush(heap, task_delays[top])
            
            intervals += 1
        return intervals

class PriorityQueue():
    def __init__(self, tasks, n):
        counts = defaultdict(int)
        for t in tasks:
            counts[t] += 1
        self.n = n
        self.intervals = 0
        self.backlog = counts
        self.queue = [0]
        self.queue_len = 0
        self.priorities = {}
        for t in counts:
            self.queue.append(t)
            self.priorities[t] = [0, -counts[t]]
        self.queue_len = len(counts)
        self.build_queue()
    
    def is_empty(self):
        return self.queue_len == 0

    def pop(self):
        #pop and/or update priorities
        if not self.is_empty():            
            t = self.queue[1]
            self.priorities[t][1] += 1
            if self.priorities[t][1] < 0:
                self.priorities[t][0] = self.n + 1
            else:
                del self.backlog[t]
            popped = self.queue.pop()
            self.queue_len -= 1
            if self.queue_len != 0:
                self.queue[1] = popped
            self.heapify(1)


        for t in self.backlog.copy():
            if self.priorities[t][0] == 0:
                continue
            self.priorities[t][0] -= 1
            if self.priorities[t][0] == 0:
                self.queue.append(t)
                self.queue_len += 1
                self.float(self.queue_len)

        self.intervals += 1


    def float(self, i):
        p = i // 2
        if p > 0 and self.priorities[self.queue[i]] < self.priorities[self.queue[p]]:
            self.queue[i], self.queue[p] = self.queue[p], self.queue[i]
            self.float(p)

    def heapify(self, i):
        l = 2 * i
        r = 2 * i + 1
        smallest = i
        if l <= self.queue_len and self.priorities[self.queue[l]] < self.priorities[self.queue[smallest]]:
            smallest = l
        if r <= self.queue_len and self.priorities[self.queue[r]] < self.priorities[self.queue[smallest]]:
            smallest = r
        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self.heapify(smallest)
    
    def build_queue(self):
        for i in range(self.queue_len//2, 0, -1):
            self.heapify(i)
            

        
class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = PriorityQueue(tasks, n)
        while pq.backlog:
            pq.pop()
        return pq.intervals
