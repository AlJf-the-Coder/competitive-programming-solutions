class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        has_x = has_y = has_z = False
        x, y, z = target
        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            has_x = has_x or a == x
            has_y = has_y or b == y
            has_z = has_z or c == z
            if has_x and has_y and has_z:
                return True
        return False

class Solution1:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        x, y, z = target
        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            res = [max(res[0], a), max(res[1], b), max(res[2], c)]
        return res == target
