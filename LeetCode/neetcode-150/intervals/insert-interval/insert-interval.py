from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_start, n_end = newInterval
        n = len(intervals)
        res = []
        i = 0
        while i < n:
            start, end = intervals[i]
            if n_end < start:
                break
            elif end < n_start:
                res.append(intervals[i])
            elif start <= n_end:
                n_start = min(start, n_start)
                n_end = max(end, n_end)
            i += 1
        res.append([n_start, n_end])
        return res + intervals[i:]

class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n_start, n_end = newInterval
        n = len(intervals)
        res = []
        i = 0
        while i < n:
            start, end = intervals[i]
            if end >= n_start:
                break
            res.append(intervals[i])
            i += 1

        if i == n:
            res.append(newInterval)
            return res

        if start <= n_end:
            while i < n:
                start, end = intervals[i]
                #if start <= n_end <= end or start <= n_start <= end \
                #    or n_start <= start <= n_end or n_start <= end <= n_end:
                if start <= end:
                    n_start = min(start, n_start)
                    n_end = max(end, n_end)
                else:
                    break
                i += 1

        res.append([n_start, n_end])
        res.extend(intervals[i:])
        return res

class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_start, n_end = newInterval
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

