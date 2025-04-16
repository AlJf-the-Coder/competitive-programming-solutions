from typing import List

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

class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, k - 1)

    def quickselect(self, nums, k):
        def select(left, right, k):
            p = (left + right) // 2
            item = nums[p]
            nums[p], nums[right - 1] = nums[right - 1], nums[p]
            ind = left
            for i in range(left, right):
                if nums[i] < item:
                    nums[ind], nums[i] = nums[i], nums[ind]
                    ind += 1
            nums[ind], nums[right - 1] = nums[right - 1], nums[ind]
            if right - ind - 1 == k:
                return nums[ind]
            elif right - ind - 1 < k:
                return select(left, ind, k - (right - ind))
            else:
                return select(ind + 1, right, k)

        return select(0, len(nums), k)

