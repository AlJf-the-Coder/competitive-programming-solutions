class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        inds = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in inds:
                inds[s[i]] = i

        part_end = 0
        lengths = []
        l = r = 0
        while True:
            part_end = max(part_end, inds[s[r]])
            if part_end == len(s) - 1:
                lengths.append(len(s) - l)
                break
            elif r == part_end:
                lengths.append(r - l + 1)
                l = r = part_end + 1
            else:
                r += 1

        return lengths

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        inds = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in inds:
                inds[s[i]] = i

        part_end = 0
        lengths = []
        l = r = 0
        while r < len(s):
            part_end = max(part_end, inds[s[r]])
            if r == part_end:
                lengths.append(r - l + 1)
                l = r = part_end + 1
            else:
                r += 1
        return lengths
