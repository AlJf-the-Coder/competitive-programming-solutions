from collections import defaultdict
from math import ceil
class TimeMap:

    def __init__(self):
        self.dict = defaultdict(dict)
        self.key_timestamps = defaultdict(list)
        self.key_counts = defaultdict(int)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key][timestamp] = value
        self.key_timestamps[key].append(timestamp)
        self.key_counts[key] += 1

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        l = 0
        r = self.key_counts[key] - 1
        stamps = self.key_timestamps[key]
        if stamps[l] > timestamp:
            return ""
        while l < r:
            mid = ceil((l + r) / 2)
            if stamps[mid] <= timestamp:
                l = mid
            else:
                r = mid - 1
        return self.dict[key][stamps[l]]
        


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
