class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_len = 0
        heap = []
        for num in nums:
            if heap_len == k:
                if heap[0] < num:
                    heapq.heappop(heap)
                    heap_len -= 1
                else:
                    continue
            heapq.heappush(heap, num)
            heap_len += 1
        return heap[0]
