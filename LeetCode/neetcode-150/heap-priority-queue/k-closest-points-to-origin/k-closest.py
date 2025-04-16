import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            dist = x**2 + y**2
            if len(heap) == k:
                if dist < -heap[0][0]:
                    heapq.heappop(heap)
                else:
                    continue
            heapq.heappush(heap, [-dist, point])
        return [point for (_, point) in heap]

from math import sqrt
class Solution1:
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

class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(x**2 + y**2, [x, y]) for (x, y) in points]
        return self.quickselect(dists, k - 1)

    def quickselect(self, dists, k):
        n = len(dists)
        def select(left, right):
            item = dists[right - 1]
            ind = left
            for i in range(left, right):
                if dists[i] < item:
                    dists[ind], dists[i] = dists[i], dists[ind]
                    ind += 1
            dists[ind], dists[right - 1] = dists[right - 1], dists[ind]
            if ind == k:
                return [d[1] for d in dists[: ind + 1]]
            elif ind > k:
                return select(left, ind)
            else:
                return select(ind + 1, right)

        return select(0, n)

    def quickselect1(self, dists, k):
        n = len(dists)

        def partition(left, right):
            item = dists[right - 1]
            ind = left
            for i in range(left, right):
                if dists[i] < item:
                    dists[ind], dists[i] = dists[i], dists[ind]
                    ind += 1
            dists[ind], dists[right - 1] = dists[right - 1], dists[ind]
            return ind

        left = 0
        right = n
        ind = partition(left, right)
        while ind != k:
            if ind == k:
                break
            elif ind > k:
                right = ind
            else:
                left = ind + 1
            ind = partition(left, right)

        return [d[1] for d in dists[: ind + 1]]
