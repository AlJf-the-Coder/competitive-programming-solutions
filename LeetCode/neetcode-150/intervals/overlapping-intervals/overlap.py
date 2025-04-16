class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        new_intervals = sorted(set(map(tuple, intervals)), key=lambda i: i[0])
        count = len(intervals) - len(new_intervals)
        overlaps = [0] * len(new_intervals)
        for i in range(len(new_intervals)):
            for j in range(i + 1, len(new_intervals)):
                if new_intervals[i][1] > new_intervals[j][0]:
                    overlaps[i] += 1
                    overlaps[j] += 1
        while any(overlaps):
            ind = max(range(len(new_intervals)), key=lambda i: overlaps[i])
            count += 1
            overlaps[ind] = 0
            for j in range(ind + 1, len(new_intervals)):
                if overlaps[j] and new_intervals[ind][1] > new_intervals[j][0]:
                    overlaps[j] -= 1
            for j in range(0, ind):
                if overlaps[j] and new_intervals[j][1] > new_intervals[ind][0]:
                    overlaps[j] -= 1
        return count
