class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        queue = deque()
        l = r = 0

        while r < len(nums):
            if r - l == k:
                maxes.append(queue[0])
                if queue[0] == nums[l]:
                    queue.popleft()
                l += 1
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])
            r += 1
        maxes.append(queue[0])
        return maxes

class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        maxes = [queue[0]]

        for i in range(1, len(nums) - k + 1):
            if queue[0] == nums[i - 1]:
                queue.popleft()
            while queue and queue[-1] < nums[i + k - 1]:
                queue.pop()
            queue.append(nums[i + k - 1])
            maxes.append(queue[0])
        return maxes

import heapq
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        item_finder = []
        max_heap = []
        for i in range(k):
            item = [-nums[i], True]
            heapq.heappush(max_heap, item)
            item_finder.append(item)
        maxes = [-max_heap[0][0]]

        for i in range(1, len(nums) - k + 1):
            item_finder[i - 1][1] = False
            item = [-nums[i + k - 1], True]
            item_finder.append(item)
            heapq.heappush(max_heap, item)
            while not max_heap[0][1]:
                heapq.heappop(max_heap)
            maxes.append(-max_heap[0][0])
        return maxes
