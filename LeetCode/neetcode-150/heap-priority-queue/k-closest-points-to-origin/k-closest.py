import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heap_len = 0
        for point in points:
            x, y = point
            dist = sqrt(x**2 + y**2)
            if heap_len == k:
                if dist < -heap[0][0]:
                    heapq.heappop(heap)
                    heap_len -= 1
                else:
                    continue
            heapq.heappush(heap, [-dist, point])
            heap_len += 1
        return [point for (_, point) in heap]
