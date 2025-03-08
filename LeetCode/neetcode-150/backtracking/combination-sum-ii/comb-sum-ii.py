class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)
        def help(arr, arr_sum, i):
            if arr_sum == target:
                res.append(arr)
            for j in range(i, n):
                if arr_sum + candidates[j] > target:
                    return
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                help(arr + [candidates[j]], arr_sum + candidates[j], j + 1)
        help([], 0, 0)
        return res

class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        counts = {}
        for num in candidates:
            counts[num] = 1 + counts.get(num, 0)
        keys = list(counts.keys())
        n = len(counts)
        def help(arr, arr_sum, i):
            if arr_sum > target:
                return
            if i == n:
                if arr_sum == target:
                    res.append(arr)
                return
            add = []
            add_sum = 0
            for _ in range(counts[keys[i]]):
                add_sum += keys[i]
                add.append(keys[i])
                help(arr + add, arr_sum + add_sum, i + 1)
            help(arr, arr_sum, i + 1)
        help([], 0, 0)
        return res
