import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.len = 0
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if self.heap:
            if self.len == self.k:
                if self.heap[0] < val:
                    heapq.heappop(self.heap)
                    self.len -= 1
                else:
                    return self.heap[0]
        heapq.heappush(self.heap, val)
        self.len += 1
        return self.heap[0]

