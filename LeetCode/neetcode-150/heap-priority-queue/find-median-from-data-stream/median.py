from collections import deque
class MedianFinder:

    def __init__(self):
        self.max_heap = [] #left
        self.min_heap = [] #right

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap)) 
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap)) 

    def addNum1(self, num: int) -> None:
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            left = -heapq.heappop(self.max_heap)
            right = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, right)
            heapq.heappush(self.min_heap, left)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
class MedianFinder1:

    def __init__(self):
        self.max_heap = deque() #left
        self.min_heap = deque() #right

    def insert_inorder(self, deq, num):
        i = 0
        while i < len(deq):
            if deq[i] > num:
                break
            i += 1
        deq.insert(i, num)

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            self.insert_inorder(self.min_heap, num)
        else:
            self.insert_inorder(self.max_heap, num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            self.insert_inorder(self.min_heap, self.max_heap.pop()) 
        elif len(self.min_heap) - len(self.max_heap) > 1:
            self.insert_inorder(self.max_heap, self.min_heap.popleft())

    def findMedian(self) -> float:
        print(self.max_heap, self.min_heap)
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return self.max_heap[-1]
        else:
            return (self.max_heap[-1] + self.min_heap[0]) / 2
