class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals:
            n_end = res[-1][1]
            if n_end >= start:
                res[-1][1] =  max(end, n_end)           
            else:
                res.append([start, end])   
        return res

class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        r = 0
        n_start, n_end = intervals[0]
        while r < len(intervals):
            start, end = intervals[r]
            if n_end < start:
                res.append([n_start, n_end])                
                n_start, n_end = intervals[r]
            else:
                n_start = min(start, n_start)
                n_end = max(end, n_end)
            r += 1
        res.append([n_start, n_end])
        return res

class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = []
        for i in range(len(intervals)):
            res = self.insert(res, intervals[i])
        return res

    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        n_start, n_end = new_interval
        n = len(intervals)
        res = []
        i = 0
        while i < n:
            start, end = intervals[i]
            if start <= n_start and n_end <= end:
                return intervals
            elif n_end < start:
                return res + [[n_start, n_end]] + intervals[i:]
            elif start <= n_end <= end:
                return res + [[n_start, end]] + intervals[i + 1:]
            elif start <= n_start <= end:
                n_start = start
            elif n_start < start and end < n_end:
                pass
            else:
                res.append(intervals[i])
            i += 1
        return res + [[n_start, n_end]]
