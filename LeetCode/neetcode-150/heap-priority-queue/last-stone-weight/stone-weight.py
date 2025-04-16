import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-stone for stone in stones]
        heapq.heapify(stone_heap)
        while len(stone_heap) > 1:
            x = -heapq.heappop(stone_heap)
            y = -heapq.heappop(stone_heap)
            if x > y:
                heapq.heappush(stone_heap, y - x)
        return -stone_heap[0] if stone_heap else 0

class Solution1:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_s = max(stones)
        weights = [0] * (max_s + 1)
        for s in stones:
            weights[s] += 1
        first = second = max_s
        while first > 0:
            if weights[first] % 2 == 0:
                first -= 1
                continue
            j = min(second, first - 1)
            while j > 0 and weights[j] == 0:
                j -= 1
            if j == 0:
                return first
            second = j
            weights[second] -= 1
            weights[first - second] += 1
            first = max(first - second, second)

        return 0
